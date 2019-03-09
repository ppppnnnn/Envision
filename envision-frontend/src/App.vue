<template>
  <v-app>
    <app-toolbar :isUserLogged=isUserLogged :ShowLoginDialog=ShowLoginDialog></app-toolbar>
    <app-side-menu :isUserLogged=isUserLogged></app-side-menu>

    <v-dialog v-model="loginDialog" max-width="450" dark>
      <v-card>
        <v-card-title class="headline">{{ loginWindowTitle }}</v-card-title>

        <v-card-text>{{ loginWindowText }} </v-card-text>

        <v-card-text>
          <v-text-field
            label="用户名"
            box
            color="amber"
            :value="inputUsername"
            :hint="hintUsername"
          ></v-text-field>
          <v-text-field
            v-if="loginWindowTitle=='注册 Envision'"
            label="邮箱"
            box
            color="amber"
            :value="inputEmail"
          ></v-text-field>
          <v-text-field
            label="密码"
            :type="passwordInputType"
            :append-icon="showPassword ? 'visibility' : 'visibility_off'"
            @click:append="TogglePasswordVisibility"
            box
            :value="inputPassword"
            color="amber"
            :hint="hintPassword"
          ></v-text-field>
        </v-card-text>

        <v-card-actions>  
          <v-btn
            color="yellow darken-1"
            flat="flat"
            @click="ToggleLoginWindowContent"
          >
            {{ loginWindowBtnLeft }}
          </v-btn>

          <v-spacer></v-spacer>

          <v-btn
            color="yellow darken-1"
            flat="flat"
          >
            {{ loginWindowBtnRight }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogLoginFailure" max-width="290">
      <v-card>
        <v-card-title class="headline">用户名或密码错误</v-card-title>
        <v-card-text>
          用户名或密码错误，登录未能成功。
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogRegFailure" max-width="290">
      <v-card>
        <v-card-title class="headline">用户名或邮箱已被注册</v-card-title>
        <v-card-text>
          您填写的用户名或者邮箱已经被注册过，注册未能成功。
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-content style="padding-right: 300px;">
      <v-container fluid>
        <v-layout>
          <v-flex shrink style="width: 100%;">
            <router-view></router-view>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>

    <app-right-side-panel></app-right-side-panel>
  </v-app>
</template>

<script>
import AppToolbar from './components/AppToolbar'
import AppSideMenu from './components/AppSideMenu'
import AppRightSidePanel from './components/AppRightSidePanel'
import axios from 'axios'
import router from './plugins/router'
import storage from './plugins/storage'

export default {
  name: 'App',
  components: {
    AppToolbar,
    AppSideMenu,
    AppRightSidePanel,
  },
  data () {
    return {
      isUserLogged: false,
      loginDialog: false,
      showPassword: false,
      passwordInputType: "password",
      loginWindowTitle: "登录 Envision",
      loginWindowBtnLeft: "没有账号？注册一个",
      loginWindowBtnRight: "登录",
      loginWindowText: "在不登录Envision的情况下，您只能访问有限的内容。登录 Envision 来让我们更好的为你服务。",
      hintUsername: "",
      hintPassword: "",
      inputUsername: "",
      inputPassword: "",
      inputEmail: "",
    }
  },
  mounted() {
    // Check local storage for user login status
    let status = this.CheckLoginStatus();

    if(status === true) {
      storage.commit('setUserId', window.localStorage.getItem(envision_uid));
      storage.commit('setUsername', window.localStorage.getItem(envision_user));
      this.isUserLogged = true;
    } else {
      this.isUserLogged = false;
    }
  },
  methods: {
    ShowLoginDialog: function() {
      this.loginDialog = true;
    },
    TogglePasswordVisibility: function() {
      if(this.passwordInputType === "password") {
        this.passwordInputType = "text";
      } else {
        this.passwordInputType = "password";
      }
      this.showPassword = !this.showPassword;
    },
    ToggleLoginWindowContent: function() {
      if(this.loginWindowTitle === "登录 Envision") {
        this.loginWindowTitle = "注册 Envision";
        this.loginWindowBtnLeft = "已有账号？去登录";
        this.loginWindowBtnRight = "注册";
        this.loginWindowText = "欢迎您注册 Envision 。注册一旦完成，Envision 会记住你的登录状态。";
        this.hintUsername = "用户名可以是汉字、字母和数字";
        this.hintPassword = "密码的长度至少是8位";
      } else {
        this.loginWindowTitle = "登录 Envision";
        this.loginWindowBtnLeft = "没有账号？注册一个";
        this.loginWindowBtnRight = "登录";
        this.loginWindowText = "在不登录Envision的情况下，您只能访问有限的内容。登录 Envision 来让我们更好的为你服务。";
        this.hintUsername = "";
        this.hintPassword = "";
      }
    },
    CheckLoginStatus: function() {
      if(window.localStorage.getItem("envision_user") != null) {
        return true;
      } else {
        return false;
      }
    },
    Login: function() {
      let self = this;
      axios.post('http://127.0.0.1:8000/login/', {
        "email_or_username": self.inputUsername,
        "password": self.inputPassword
      })
      .then(function (response) {
        console.log(response);
        if(response.data.msg == "Succeeded") {
          // successfully logged in, write ID and username into localstorage
          window.localStorage.setItem("envision_uid", "");
          window.localStorage.setItem("envision_user", self.inputUsername);
          // refresh page
          router.go('/');
        } else {
          // name or password wrong
          dialogLoginFailure = true;
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    Register: function() {
      let self = this;
      axios.post('http://127.0.0.1:8000/register/', {
        "username": self.inputUsername,
        "e_mail": self.inputEmail,
        "password": self.inputPassword
      })
      .then(function (response) {
        console.log(response);
        if(response.data.msg == "Succeeded") {
          // successfully registered
          //TODO: get ID and username, write into localstorage
          window.localStorage.setItem("envision_uid", "");
          window.localStorage.setItem("envision_user", self.inputUsername);
          router.go('/');
        } else {
          // name or email has already been registered
          dialogRegFailure = true;
        }
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style>
  * {
    font-family: 等线, Serif,sans-serif;
  }
</style>
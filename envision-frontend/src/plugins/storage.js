import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const storage = new Vuex.Store({
  state: {
		uid: "",
		username: ""
	},
	mutations: {
		setUserId (state, value) {
			state.uid = value;
		},
		setUsername (state, value) {
			state.username = value;
		}
	}
});

export default storage;
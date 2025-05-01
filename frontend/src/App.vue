<template>
  <div>
    <h1>FastAPI + Vue.js</h1>
    <button @click="fetchHello">Get Data</button>
    <p v-if="message">{{ message }}</p>

    <input v-model="inputText" placeholder="Type something">
    <button @click="sendEcho">Echo</button>
    <p v-if="echoResponse">{{ echoResponse }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: '',
      inputText: '',
      echoResponse: ''
    }
  },
  methods: {
    async fetchHello() {
      const res = await fetch('http://localhost:8000/api/hello');
      const data = await res.json();
      this.message = data.message;
    },
    async sendEcho() {
      const res = await fetch('http://localhost:8000/api/echo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: this.inputText })
      });
      this.echoResponse = (await res.json()).echo.text;
    }
  }
}
</script>
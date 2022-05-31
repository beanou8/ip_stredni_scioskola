// Firebase DB
firebase.initializeApp({
    apiKey: "AIzaSyAYeXoaNgG32E-rLr6BVA3UvFpPpFBJ8Rw",
    authDomain: "login-vue-6463e.firebaseapp.com",
    projectId: "login-vue-6463e"
});

const db = firebase.firestore();

let articles = []

db.collection("users").get().then((querySnapshot) => {
    querySnapshot.forEach((doc) => {
        const d = {
            'id': doc.id,
            'data': doc.data()
        }
        console.log(d)
        //articles.append(d);
    });
});

console.log(articles)

import { createApp,reactive } from 'https://unpkg.com/petite-vue?module'

// Vue code
const store = reactive({
    count: 0,
    inc() {
        db.collection("users").doc("count").set({
            c: this.count++
        })
            .then(() => {
                console.log("Document successfully written!");
            })
            .catch((error) => {
                console.error("Error writing document: ", error);
            });
    }
})

createApp({
    store,
    addOne() {
        store.inc()
    }
}).mount()
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBbeBd4rnnlZdVve9sB3pziJxcmi7kYpkA",
    authDomain: "gcp-codebase.firebaseapp.com",
    projectId: "gcp-codebase",
    storageBucket: "gcp-codebase.firebasestorage.app",
    messagingSenderId: "577880148572",
    appId: "1:577880148572:web:0a0fee4684f0b2726a3499",
    measurementId: "G-MRSPQZW21X"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);

export default app;
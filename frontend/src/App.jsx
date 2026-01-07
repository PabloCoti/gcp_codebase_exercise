import './App.css'
import { useState, useEffect } from 'react';
import { signInWithPopup, GoogleAuthProvider, onAuthStateChanged, signOut } from 'firebase/auth';
import { auth } from './config/firebase';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
    });

    return () => unsubscribe();
  }, []);

  const signIn = () => {
    signInWithPopup(auth, new GoogleAuthProvider());
  };

  const handleSignOut = () => {
    signOut(auth);
  };

  return (
    <>
      {user ? (
        <>
          <p>You are logged in as {user.email}</p>
          <button onClick={handleSignOut}>Log out</button>
        </>
      ) : (
        <button onClick={signIn}>Sign in</button>
      )}
    </>
  )
}

export default App

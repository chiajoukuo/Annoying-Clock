import React, { Component } from 'react';
import './App.css';
// import firebase from 'firebase';
import firebase from 'firebase';
import TimePicker from './TimePicker'

class App extends Component {
  constructor(props) {
    super(props);
    // const firebaseConfig = {
    //   apiKey: "AIzaSyD1uayt80Yno052cuC6EGFafqp0rm5S-Bk",
    //   authDomain: "annoying-clock.firebaseapp.com",
    //   databaseURL: "https://annoying-clock.firebaseio.com",
    //   projectId: "annoying-clock",
    //   storageBucket: "annoying-clock.appspot.com",
    //   messagingSenderId: "362764611665",
    //   appId: "1:362764611665:web:b523ba718a1297bc"
    // };
    // firebase.initializeApp(firebaseConfig);
    firebase.initializeApp({
      apiKey: "AIzaSyD1uayt80Yno052cuC6EGFafqp0rm5S-Bk",
      authDomain: "annoying-clock.firebaseapp.com",
      databaseURL: "https://annoying-clock.firebaseio.com",
      projectId: "annoying-clock",
      storageBucket: "annoying-clock.appspot.com",
      messagingSenderId: "362764611665",
      appId: "1:362764611665:web:b523ba718a1297bc"
    })
    // firebase.database().ref('/alarms').child('alarm1').once('value').then((snapshot) => {
    //   console.log(snapshot.val)
    // })
  }
  // fetchProductById (id) {
  //   var db = admin.database()
  //   var collectionRef = db.ref('server/products')
  //   var ref = collectionRef.child(id)
  //   return ref.once('value')
  //       .then((snapshot) => {
  //           return snapshot.val()
  //       })} 

  render() {
    console.log(this.firebase)
    return (
      <div className="App">
        <div>
          <TimePicker db={this.firebase} />
        </div>
      </div>
    );
  }
}

export default App;
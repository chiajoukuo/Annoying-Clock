import React, { Component } from 'react';
import './App.css';
// import firebase from 'firebase';
import firebase from 'firebase';
import TimePicker from './TimePicker'
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {
  constructor(props) {
    super(props);
    const firebaseConfig = {
      apiKey: "AIzaSyD1uayt80Yno052cuC6EGFafqp0rm5S-Bk",
      authDomain: "annoying-clock.firebaseapp.com",
      databaseURL: "https://annoying-clock.firebaseio.com",
      projectId: "annoying-clock",
      storageBucket: "annoying-clock.appspot.com",
      messagingSenderId: "362764611665",
      appId: "1:362764611665:web:b523ba718a1297bc"
    };
    firebase.initializeApp(firebaseConfig);
    // firebase.initializeApp({
    //   apiKey: "AIzaSyD1uayt80Yno052cuC6EGFafqp0rm5S-Bk",
    //   authDomain: "annoying-clock.firebaseapp.com",
    //   databaseURL: "https://annoying-clock.firebaseio.com",
    //   projectId: "annoying-clock",
    //   storageBucket: "annoying-clock.appspot.com",
    //   messagingSenderId: "362764611665",
    //   appId: "1:362764611665:web:b523ba718a1297bc"
    // })
    const db = firebase.database()
    console.log("DB:", db)
    // var alarm = db.ref('/alarm/alarm1').set({
    //   hour: 7,
    //   minute: 30
    // })
    // .then(function () {
    //   alert("建立成功");
    // }).catch(function () {
    //   alert("伺服器發生錯誤，請稍後再試");
    // });
    // console.log("ALARM", alarm)
    // //.ref('/alarms').child('alarm1').once('value').then((snapshot) => {
    // //   console.log(snapshot.val)
    // // })
  }

  render() {
    console.log(firebase)
    return (
      <div className="App">
        <section className="jumbotron-header header">
          <h1 className="jumbotron-heading display-2">Annoying Alarm</h1>
          <p className="lead mt-5 display-4">Set your alarm time below</p>
          <div className="picker">
            <TimePicker db={firebase} />
          </div>
        </section>
      </div>
    );
  }
}

export default App;
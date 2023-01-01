import axios from "axios";

axios.post('https://IsolatedSoul.pythonanywhere.com/score', {
    'score': '',
  })
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
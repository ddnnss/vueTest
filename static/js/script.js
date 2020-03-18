 Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})

var app = new Vue({
   delimiters : ['[[',']]'],
  el: '#app',
   data: () => {
      return {
          fname: '',
          message: 'dsfdsf',
          groceryList: [


         ]
      }
    },
    methods:{
       sendreq: function(){
           console.log('this.fname',this.fname)
           axios.post('http://localhost:8000/entry/',{  fname: this.fname, lname: this.lname, age: this.age })
            .then(response => this.responseData = response.data)
               console.log('ok')
            .catch(error => {
                console.log('error')

            });
       }
    }

})
function newPage1()  {
    window.location.href = 'http://127.0.0.1:8000/Christmaspage/'
}
function newPage2()  {
    window.location.href = 'http://127.0.0.1:8000/Endyearpage/'
}
function newPage3()  {
    window.location.href = 'http://127.0.0.1:8000/Newyearpage/'
}
function newPage4()  {
    window.location.href = 'http://127.0.0.1:8000/Christmaspage/'
}

function newPage5()  {
    window.location.href = 'http://127.0.0.1:8000/ResultXmas/'
}
function newPage6()  {
    window.location.href = 'http://127.0.0.1:8000/ResultYearEnd/'
}
function newPage7()  {
    window.location.href = 'http://127.0.0.1:8000/ResultNewyear/'
}
// 클릭시 페이지 이동
let whoSend
function bringClickValue(arg0){
  var value = $(arg0).val();
  whoSend = value;


}

function changeWho(){ // 누구에게 보낼지 변경
  let whois = document.getElementById('who');
  whois.innerHTML = whoSend;

}



// 버튼 클릭시 스타일 변경
//첫 번째 버튼
var category = document.getElementsByClassName("category");

      function handleClick1(event) {
        console.log(event.target);
        // console.log(this);
        // 콘솔창을 보면 둘다 동일한 값이 나온다

        console.log(event.target.classList);

        if (event.target.classList[1] === "clicked") {

          event.target.classList.remove("clicked");
        } else {
          for (var i = 0; i < category.length; i++) {

            category[i].classList.remove("clicked");
          }

          event.target.classList.add("clicked");
        }
      }

      function init() {
        for (var i = 0; i < category.length; i++) {
            flag = 1 ;
            category[i].addEventListener("click", handleClick1);
        }
      }

      init();
//두 번째 버튼
var sendTo = document.getElementsByClassName("sendTo");


      function handleClick2(event) {
        changeWho();
        console.log(event.target);
        // console.log(this);
        // 콘솔창을 보면 둘다 동일한 값이 나온다

        console.log(event.target.classList);

        if (event.target.classList[1] === "clicked1") {
          event.target.classList.remove("clicked1");
        } else {
          for (var i = 0; i < sendTo.length; i++) {
            sendTo[i].classList.remove("clicked1");
          }

          event.target.classList.add("clicked1");
        }
      }

      function init1() {
        for (var i = 0; i < sendTo.length; i++) {
          sendTo[i].addEventListener("click", handleClick2);

        }
      }

init1();



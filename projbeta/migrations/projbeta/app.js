let timerStarted = true;
document.getElementsByName('words')[0].oninput = function(){
    if(timerStarted){
        let sec = 10;
        let time = setInterval(()=>{
            let new_sec = sec--;
            if(new_sec===0){
                clearInterval(time)
                document.getElementById('form').submit();
                return;
            }
            document.getElementById('timer').innerHTML = new_sec
        },1000)
        timerStarted = false;
    }
}
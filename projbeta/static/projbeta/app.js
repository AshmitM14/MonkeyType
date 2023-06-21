let timerStarted = false;
let timer;

document.getElementsByName('words')[0].oninput = function() {
    if (!timerStarted) {
        startTimer();
        timerStarted = true;
    }
};

function startTimer() {
    let sec = 30;
    timer = setInterval(() => {
        let new_sec = sec--;
        if (new_sec === 0) {
            clearInterval(timer);
            document.getElementById('form').submit();
            return;
        }
        document.getElementById('timer').innerHTML = new_sec;
    }, 1000);
}

document.getElementById('re').onclick = function() {
    clearInterval(timer);
    document.getElementsByName('words')[0].value = '';
    document.getElementById('timer').innerHTML = '';
    timerStarted = false;
};




let questions = [];
let current = 0;
let results = [];

const questionContainer = document.getElementById('question-container');
const questionEl = document.getElementById('question');
const optionsEl = document.getElementById('options');
const resultEl = document.getElementById('result');
const shareBtn = document.getElementById('share');

fetch('/quiz')
  .then(res => res.json())
  .then(data => {
    questions = data;
    showQuestion();
  });

function showQuestion() {
  const q = questions[current];
  questionEl.textContent = q.question;
  optionsEl.innerHTML = '';
  q.options.forEach((opt, idx) => {
    const btn = document.createElement('button');
    btn.textContent = opt;
    btn.addEventListener('click', () => handleAnswer(btn, idx === q.correct_index));
    optionsEl.appendChild(btn);
  });
  questionContainer.classList.remove('hidden');
}

function handleAnswer(btn, correct) {
  Array.from(optionsEl.children).forEach(b => b.disabled = true);
  btn.classList.add(correct ? 'correct' : 'wrong');
  results.push(correct);
  setTimeout(() => {
    current++;
    if (current < questions.length) {
      showQuestion();
    } else {
      showResult();
    }
  }, 800);
}

function showResult() {
  questionContainer.classList.add('hidden');
  const score = results.filter(Boolean).length;
  const emoji = results.map(r => (r ? '🟩' : '🟥')).join('');
  resultEl.textContent = `Score: ${score}/${results.length}\n${emoji}`;
  resultEl.classList.remove('hidden');
  shareBtn.classList.remove('hidden');
  shareBtn.onclick = () => {
    const shareText = `RBI Quiz ${score}/${results.length}\n${emoji}\n${window.location.href}`;
    navigator.clipboard.writeText(shareText);
    shareBtn.textContent = 'Copied!';
    setTimeout(() => (shareBtn.textContent = 'Share'), 2000);
  };
}

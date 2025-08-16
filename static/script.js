let questions = [];
let current = 0;
let correctCount = 0;
let results = [];

const qCountEl = document.getElementById('q-count');
const correctCountEl = document.getElementById('correct-count');
const progressBar = document.getElementById('progress');
const difficultyEl = document.getElementById('difficulty');
const questionEl = document.getElementById('question');
const optionsEl = document.getElementById('options');
const feedbackEl = document.getElementById('feedback');
const nextBtn = document.getElementById('next');
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
  qCountEl.textContent = `${current + 1}/${questions.length}`;
  correctCountEl.textContent = `${correctCount} correct`;
  progressBar.style.width = `${(current / questions.length) * 100}%`;
  difficultyEl.textContent = q.difficulty;
  questionEl.textContent = q.question;
  optionsEl.innerHTML = '';
  q.options.forEach((opt, idx) => {
    const btn = document.createElement('button');
    btn.textContent = opt;
    btn.className = 'option';
    btn.onclick = () => selectAnswer(idx);
    optionsEl.appendChild(btn);
  });
  nextBtn.classList.add('hidden');
  feedbackEl.className = 'hidden';
  feedbackEl.textContent = '';
}

function selectAnswer(idx) {
  const q = questions[current];
  Array.from(optionsEl.children).forEach((btn, bIdx) => {
    btn.disabled = true;
    if (bIdx === q.correct_index) btn.classList.add('correct');
    if (bIdx === idx && bIdx !== q.correct_index) btn.classList.add('wrong');
  });
  if (idx === q.correct_index) {
    correctCount++;
    results.push(true);
    feedbackEl.textContent = 'Correct!';
    feedbackEl.className = 'correct';
  } else {
    results.push(false);
    feedbackEl.textContent = `Wrong! Correct answer: ${q.options[q.correct_index]}`;
    feedbackEl.className = 'wrong';
  }
  correctCountEl.textContent = `${correctCount} correct`;
  nextBtn.classList.remove('hidden');
}

nextBtn.onclick = () => {
  current++;
  if (current < questions.length) {
    showQuestion();
  } else {
    showResult();
  }
};

function showResult() {
  qCountEl.textContent = `${questions.length}/${questions.length}`;
  progressBar.style.width = `100%`;
  difficultyEl.classList.add('hidden');
  questionEl.classList.add('hidden');
  optionsEl.classList.add('hidden');
  nextBtn.classList.add('hidden');
  const emoji = results.map(r => (r ? '🟩' : '🟥')).join('');
  resultEl.textContent = `Score: ${correctCount}/${questions.length}\n${emoji}`;
  resultEl.classList.remove('hidden');
  shareBtn.classList.remove('hidden');
  shareBtn.onclick = () => {
    const shareText = `RBI Quiz Quest ${correctCount}/${questions.length}\n${emoji}\n${window.location.href}`;
    navigator.clipboard.writeText(shareText);
    shareBtn.textContent = 'Copied!';
    setTimeout(() => (shareBtn.textContent = 'Share'), 2000);
  };
}

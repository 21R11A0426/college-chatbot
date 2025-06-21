class VoiceChatBot {
  constructor() {
    this.messages = [];
    this.isListening = false;
    this.isSpeaking = false;
    this.isVoiceEnabled = true;
    this.recognition = null;
    this.synthesis   = window.speechSynthesis;

    this.initElements();
    this.initSpeechRecognition();
    this.addWelcomeMessage();
    this.setupListeners();
    this.updateUI();
  }

  initElements() {
    this.msgContainer = document.getElementById('messages');
    this.textInput    = document.getElementById('textInput');
    this.voiceBtn     = document.getElementById('voiceBtn');
    this.volumeBtn    = document.getElementById('volumeBtn');
    this.sendBtn      = document.getElementById('sendBtn');
    this.chatForm     = document.getElementById('chatForm');
    this.status       = document.getElementById('status');
  }

  initSpeechRecognition() {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
      this.recognition = new SR();
      this.recognition.continuous = false;
      this.recognition.interimResults = false;
      this.recognition.lang = 'en-US';

      this.recognition.onstart = () => { this.isListening = true; this.updateUI(); };
      this.recognition.onresult = e => {
        const txt = e.results[0][0].transcript;
        this.handleSend(txt);
      };
      this.recognition.onend   = () => { this.isListening = false; this.updateUI(); };
      this.recognition.onerror = () => { this.isListening = false; this.updateUI(); };
    } else {
      this.status.textContent = 'Voice input not supported';
      this.voiceBtn.disabled = true;
    }
  }

  setupListeners() {
    this.chatForm.addEventListener('submit', e => {
      e.preventDefault();
      const txt = this.textInput.value.trim();
      if (!txt) return;
      this.handleSend(txt);
      this.textInput.value = '';
    });

    this.voiceBtn.addEventListener('click', () => {
      if (this.isListening) this.recognition.stop();
      else this.recognition.start();
    });

    this.volumeBtn.addEventListener('click', () => {
      this.isVoiceEnabled = !this.isVoiceEnabled;
      if (!this.isVoiceEnabled && this.isSpeaking) {
        this.synthesis.cancel();
        this.isSpeaking = false;
      }
      this.updateUI();
    });
  }

  addWelcomeMessage() {
    this.addMessage({
      text: "Hello! I'm your college assistant. Ask me about classes, college info, weather, etc.",
      isUser: false,
      timestamp: new Date()
    });
  }

  addMessage(msg) {
    const div = document.createElement('div');
    div.className = `message ${msg.isUser ? 'user' : 'bot'}`;
    div.innerHTML = `
      <div class="message-content">
        <div>${msg.text}</div>
        <div class="timestamp">${msg.timestamp.toLocaleTimeString()}</div>
      </div>`;
    this.msgContainer.appendChild(div);
    this.msgContainer.scrollTop = this.msgContainer.scrollHeight;
  }

  updateUI() {
    // voice button state
    if (this.isListening) {
      this.voiceBtn.classList.add('listening');
      this.voiceBtn.textContent = '🎙️';
    } else {
      this.voiceBtn.classList.remove('listening');
      this.voiceBtn.textContent = '🎤';
    }
    // volume button state
    if (this.isVoiceEnabled) {
      this.volumeBtn.classList.remove('muted');
      this.volumeBtn.textContent = '🔊';
    } else {
      this.volumeBtn.classList.add('muted');
      this.volumeBtn.textContent = '🔇';
    }
    // status text
    if (this.isListening) {
      this.status.innerHTML = '<div class="status-indicator listening"><div class="status-dot"></div>Listening...</div>';
    } else if (this.isSpeaking) {
      this.status.innerHTML = '<div class="status-indicator speaking"><div class="status-dot"></div>Speaking...</div>';
    } else {
      this.status.textContent = 'Ready to chat!';
    }
  }

  async handleSend(text) {
    if (!text.trim()) return;
    // add user
    this.addMessage({ text, isUser: true, timestamp: new Date() });

    try {
      const res = await fetch('/chat', {
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify({ message: text })
      });
      const { response } = await res.json();
      this.addMessage({ text: response, isUser: false, timestamp: new Date() });
      this.speak(response);
    } catch {
      this.addMessage({ text: "Server error.", isUser: false, timestamp: new Date() });
    }
  }

  speak(text) {
    if (!this.isVoiceEnabled) return;
    this.synthesis.cancel();
    this.isSpeaking = true;
    this.updateUI();

    const utt = new SpeechSynthesisUtterance(text);
    utt.onend = () => { this.isSpeaking = false; this.updateUI(); };
    utt.onerror = () => { this.isSpeaking = false; this.updateUI(); };
    utt.rate = 0.9;
    this.synthesis.speak(utt);
  }
}

// Instantiate on load
window.addEventListener('DOMContentLoaded', () => new VoiceChatBot());

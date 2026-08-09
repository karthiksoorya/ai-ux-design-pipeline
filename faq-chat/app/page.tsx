'use client';

import { useChat } from '@ai-sdk/react';
import { DefaultChatTransport } from 'ai';
import { FormEvent, useEffect, useMemo, useRef, useState } from 'react';

const suggestions = [
  'What makes the Requirements Challenge Agent different?',
  'Explain Advocate, Cynic, and Debate Synthesis.',
  'How do the D1–D4 human gates work?',
  'What is the difference between Demo and Live AI mode?',
  'When is the prototype considered verified?',
  'Does the pipeline accept inputs beyond a BRD?',
];

function textFor(message: { parts: Array<{ type: string; text?: string }> }) {
  return message.parts.filter((part) => part.type === 'text').map((part) => part.text ?? '').join('');
}

export default function Home() {
  const [input, setInput] = useState('');
  const [password, setPassword] = useState('');
  const passwordRef = useRef('');
  const endRef = useRef<HTMLDivElement>(null);
  const transport = useMemo(() => new DefaultChatTransport({ api: '/api/chat' }), []);
  const { messages, sendMessage, status, error, stop, setMessages } = useChat({ transport });
  const busy = status === 'submitted' || status === 'streaming';

  useEffect(() => {
    const saved = window.sessionStorage.getItem('faq-chat-password') ?? '';
    setPassword(saved);
    passwordRef.current = saved;
  }, []);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth', block: 'end' });
  }, [messages, status]);

  function updatePassword(value: string) {
    setPassword(value);
    passwordRef.current = value;
    window.sessionStorage.setItem('faq-chat-password', value);
  }

  function ask(question: string) {
    if (busy || !question.trim()) return;
    sendMessage(
      { text: question.trim() },
      { headers: { 'x-faq-password': passwordRef.current } },
    );
    setInput('');
  }

  function submit(event: FormEvent) {
    event.preventDefault();
    ask(input);
  }

  return (
    <main className="app-shell">
      <aside className="context-panel">
        <a className="brand" href="https://karthiksoorya.github.io/ai-ux-design-pipeline/">
          <span className="brand-mark">AI</span>
          <span>UX Pipeline</span>
        </a>
        <div className="context-copy">
          <p className="eyebrow">GROUNDED PROJECT ASSISTANT</p>
          <h1>Ask the<br /><span>pipeline.</span></h1>
          <p>Explore the agents, skills, gates, outputs, evidence rules, and runnable demonstration.</p>
        </div>
        <div className="pipeline-mini" aria-label="Pipeline phases">
          {['Discover', 'Define & Ideate', 'Design & Prototype', 'Validate'].map((phase, index) => (
            <div key={phase}><i>{index + 1}</i><span>{phase}</span>{index < 3 && <b>↓</b>}</div>
          ))}
        </div>
        <div className="source-note">
          <span className="live-dot" />
          <div><b>Evidence-aware answers</b><small>Grounded in approved project documentation</small></div>
        </div>
        <nav>
          <a href="https://ai-ux-design-pipeline.streamlit.app/">Run pipeline ↗</a>
          <a href="https://karthiksoorya.github.io/ai-ux-design-pipeline/prototype/">Open prototype ↗</a>
          <a href="https://github.com/karthiksoorya/ai-ux-design-pipeline">View source ↗</a>
        </nav>
      </aside>

      <section className="chat-panel">
        <header className="chat-header">
          <div><p>AI UX PIPELINE GUIDE</p><h2>Project FAQ Assistant</h2></div>
          <div className="mode-badge"><span /> Gemini · Grounded</div>
        </header>

        <div className="chat-scroll" aria-live="polite">
          {messages.length === 0 ? (
            <div className="welcome">
              <div className="assistant-avatar">AI</div>
              <p className="eyebrow">WELCOME</p>
              <h2>What would you like to understand?</h2>
              <p>I answer questions about this project’s architecture and demonstration. Choose a starting point or ask your own question.</p>
              <div className="suggestions">
                {suggestions.map((question) => <button key={question} onClick={() => ask(question)}>{question}<span>→</span></button>)}
              </div>
            </div>
          ) : (
            <div className="messages">
              {messages.map((message) => (
                <article className={`message ${message.role}`} key={message.id}>
                  <div className="avatar">{message.role === 'user' ? 'YOU' : 'AI'}</div>
                  <div><p className="message-label">{message.role === 'user' ? 'Your question' : 'Pipeline guide'}</p><div className="bubble">{textFor(message)}</div></div>
                </article>
              ))}
              {status === 'submitted' && <div className="thinking"><span /><span /><span /> Reviewing project knowledge…</div>}
            </div>
          )}
          {error && <div className="error-card"><b>Couldn’t answer that request.</b><span>{error.message.includes('401') ? 'Check the access password and try again.' : error.message}</span></div>}
          <div ref={endRef} />
        </div>

        <div className="composer-wrap">
          <div className="access-row">
            <label htmlFor="password">Access password</label>
            <input id="password" type="password" value={password} onChange={(event) => updatePassword(event.target.value)} placeholder="Required when configured" autoComplete="current-password" />
            {messages.length > 0 && <button className="new-chat" onClick={() => setMessages([])}>New chat</button>}
          </div>
          <form className="composer" onSubmit={submit}>
            <textarea value={input} onChange={(event) => setInput(event.target.value)} onKeyDown={(event) => { if (event.key === 'Enter' && !event.shiftKey) { event.preventDefault(); ask(input); } }} placeholder="Ask about agents, phases, gates, evidence, inputs, or outputs…" rows={2} maxLength={1200} disabled={busy} />
            {busy ? <button className="send stop" type="button" onClick={stop} aria-label="Stop response">■</button> : <button className="send" type="submit" disabled={!input.trim()} aria-label="Send question">↑</button>}
          </form>
          <p className="disclaimer">AI answers can be imperfect. Verify important details in the <a href="https://karthiksoorya.github.io/ai-ux-design-pipeline/">project documentation</a>.</p>
        </div>
      </section>
    </main>
  );
}

# AI UX Pipeline FAQ Chat

A Vercel-ready conversational FAQ for the AI UX Discovery-to-Prototype Pipeline. It uses Gemini through a server-only Next.js route and restricts answers to the approved project knowledge in `lib/knowledge.ts`.

## Local setup

1. Copy `.env.example` to `.env.local`.
2. Add `GEMINI_API_KEY` and an optional shared `FAQ_CHAT_PASSWORD`.
3. Run `npm install` and `npm run dev`.

## Vercel setup

- Import the existing GitHub repository as a new Vercel project.
- Set **Root Directory** to `faq-chat`.
- Keep **Framework Preset** as Next.js.
- Add `GEMINI_API_KEY` and `FAQ_CHAT_PASSWORD` under Project Settings → Environment Variables.
- Apply both variables to Production and Preview, then deploy.

The browser never receives the Gemini API key. The shared password is sent to the same-origin server route and kept only in the browser session; it is a demo safeguard, not enterprise authentication.

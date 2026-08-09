import { createGoogle } from '@ai-sdk/google';
import {
  convertToModelMessages,
  createUIMessageStreamResponse,
  streamText,
  toUIMessageStream,
  type UIMessage,
} from 'ai';
import { SYSTEM_INSTRUCTIONS } from '../../../lib/knowledge';

export const runtime = 'nodejs';
export const maxDuration = 30;

function unauthorized() {
  return Response.json({ error: 'The FAQ chat password is incorrect.' }, { status: 401 });
}

export async function POST(request: Request) {
  const configuredPassword = process.env.FAQ_CHAT_PASSWORD?.trim();
  const suppliedPassword = request.headers.get('x-faq-password')?.trim();

  if (configuredPassword && suppliedPassword !== configuredPassword) {
    return unauthorized();
  }

  const apiKey = process.env.GEMINI_API_KEY?.trim();
  if (!apiKey) {
    return Response.json(
      { error: 'Gemini is not configured. Add GEMINI_API_KEY in Vercel.' },
      { status: 503 },
    );
  }

  let body: { messages?: UIMessage[] };
  try {
    body = await request.json();
  } catch {
    return Response.json({ error: 'Invalid request.' }, { status: 400 });
  }

  const messages = Array.isArray(body.messages) ? body.messages.slice(-12) : [];
  const characterCount = JSON.stringify(messages).length;
  if (!messages.length || characterCount > 24000) {
    return Response.json({ error: 'The conversation is empty or too long. Start a new chat.' }, { status: 400 });
  }

  const google = createGoogle({ apiKey });
  const result = streamText({
    model: google('gemini-2.5-flash'),
    instructions: SYSTEM_INSTRUCTIONS,
    messages: await convertToModelMessages(messages),
    temperature: 0.2,
    maxOutputTokens: 700,
  });

  return createUIMessageStreamResponse({
    stream: toUIMessageStream({ stream: result.stream }),
  });
}

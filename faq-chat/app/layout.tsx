import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Ask the AI UX Pipeline',
  description: 'A grounded Gemini-powered FAQ assistant for the AI UX Discovery-to-Prototype Pipeline.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

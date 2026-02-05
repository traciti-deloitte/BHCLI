import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "BHCLI Impact OS",
  description: "Internal platform for BHCLI impact evidence, graphs, and story studio."
};

export default function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

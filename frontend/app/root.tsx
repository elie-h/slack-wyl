import {
  Links,
  LiveReload,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";
import { Analytics } from "@vercel/analytics/react";

import type { LinksFunction } from "@remix-run/node";

import { Footer } from "~/components/footer";
import { Header } from "~/components/header";
import stylesheet from "~/tailwind.css";

export const links: LinksFunction = () => [
  { rel: "stylesheet", href: stylesheet },
];

export default function App() {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body className="bg-background text-text-primary dark:bg-d-background dark:text-d-text-primary">
        <div className="flex min-h-screen flex-col">
          <Header />
          <div className="relative">
            <Outlet />
          </div>
          <Footer />
        </div>
        <ScrollRestoration />
        <Scripts />
        {process.env.NODE_ENV === "production" && <Analytics />}
        <LiveReload />
      </body>
    </html>
  );
}

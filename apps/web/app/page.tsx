const topics = [
  "Collaboration",
  "Data & Evidence",
  "Innovation",
  "Strategic Leadership & Management"
];

const cards = [
  {
    eyebrow: "Latest insight",
    title: "Draft claims needing review",
    body: "Review high-priority claims awaiting evidence validation and confidence ratings.",
    meta: ["Impact Editor", "12 items"]
  },
  {
    eyebrow: "Cities to watch",
    title: "Capability gains across cohorts",
    body: "Track cohort participation and emerging capability shifts across partner cities.",
    meta: ["Programs", "8 cities"]
  },
  {
    eyebrow: "Evidence coverage",
    title: "ToC nodes with low coverage",
    body: "Identify theory-of-change nodes that need additional evidence collection.",
    meta: ["Impact Ops", "6 gaps"]
  }
];

export default function Home() {
  return (
    <main>
      <header className="border-b border-fog">
        <div className="container flex items-center justify-between py-6">
          <div>
            <p className="text-sm uppercase tracking-[0.2em] text-slate">BHCLI Impact OS</p>
            <h1 className="mt-2 font-display text-4xl md:text-5xl">
              Explore evidence, capability, and impact stories
            </h1>
          </div>
          <nav className="hidden gap-6 text-sm text-slate md:flex">
            <span>Explore</span>
            <span>Graph</span>
            <span>Story Studio</span>
            <span>Dashboards</span>
            <span>Reports</span>
            <span>Admin</span>
          </nav>
        </div>
      </header>

      <section className="container py-10">
        <div className="flex flex-wrap items-center gap-3">
          {topics.map((topic) => (
            <span
              key={topic}
              className="rounded-full border border-fog bg-white px-4 py-2 text-sm text-slate"
            >
              {topic}
            </span>
          ))}
        </div>
        <div className="mt-8 grid gap-6 md:grid-cols-3">
          {cards.map((card) => (
            <article
              key={card.title}
              className="rounded-2xl border border-fog bg-white p-6 shadow-card"
            >
              <p className="text-xs uppercase tracking-[0.2em] text-brass">
                {card.eyebrow}
              </p>
              <h2 className="mt-3 text-xl font-semibold text-ink">{card.title}</h2>
              <p className="mt-3 text-sm text-slate">{card.body}</p>
              <div className="mt-5 flex flex-wrap gap-2">
                {card.meta.map((item) => (
                  <span
                    key={item}
                    className="rounded-full bg-fog px-3 py-1 text-xs text-slate"
                  >
                    {item}
                  </span>
                ))}
              </div>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

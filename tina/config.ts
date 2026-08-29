import { defineConfig } from "tinacms";

// Tina never touches HTML. It edits JSON in /content; the build regenerates pages.
// A bad edit can produce awkward wording. It cannot produce broken markup.
export default defineConfig({
  branch: process.env.TINA_BRANCH || process.env.CF_PAGES_BRANCH || "main",
  clientId: process.env.NEXT_PUBLIC_TINA_CLIENT_ID!,
  token: process.env.TINA_TOKEN!,
  build: { outputFolder: "admin", publicFolder: "." },
  media: { tina: { mediaRoot: "media", publicFolder: "." } },
  schema: {
    collections: [
      {
        name: "blog",
        label: "Journal Posts",
        path: "content/blog",
        format: "json",
        // the only collection she may add to or remove from
        ui: {
          filename: {
            readonly: false,
            slugify: (v) =>
              (v?.title || "post")
                .toLowerCase()
                .replace(/[^a-z0-9]+/g, "-")
                .replace(/^-|-$/g, "")
                .slice(0, 60),
          },
        },
        fields: [
          {
            type: "string", name: "title", label: "Title", isTitle: true, required: true,
            description: "Shown on the Journal list and used for the page title.",
          },
          {
            type: "boolean", name: "published", label: "Published", required: true,
            description:
              "Off removes the post from the site entirely, including its web address. It is not just hidden.",
          },
          {
            type: "string", name: "slug", label: "Web address", required: true,
            description: "The part after the slash. Changing this on a live post breaks existing links.",
          },
          { type: "string", name: "date", label: "Date (YYYY-MM-DD)", required: true },
          { type: "string", name: "dateLabel", label: "Date as written", description: "e.g. August 7, 2026" },
          { type: "string", name: "author", label: "Author" },
          {
            type: "string", name: "stage", label: "Framework stage",
            options: ["Awaken", "Understand", "Reconnect", "Become", "Relate"],
          },
          { type: "string", name: "stageLabel", label: "Stage line", description: 'e.g. "Stage II · Understand"' },
          { type: "string", name: "readingTime", label: "Reading time", description: 'e.g. "4 min"' },
          {
            type: "string", name: "excerpt", label: "Summary for the Journal list",
            ui: { component: "textarea" }, required: true,
          },
          {
            type: "string", name: "metaDescription", label: "Search engine description",
            ui: { component: "textarea" },
            description: "Around 155 characters. This is what shows up in Google.",
          },
          {
            type: "string", name: "titleHtml", label: "Title with line breaks",
            description:
              "Optional. Use <br> to control where the headline wraps. Leave blank to wrap automatically.",
          },
          {
            type: "string", name: "body", label: "Post", list: true, required: true,
            ui: { component: "textarea" },
            description:
              'One box per paragraph. Start a box with "## " for a heading, or "> " for a pull quote.',
          },
          { type: "string", name: "endnoteTitle", label: "Closing note heading" },
          { type: "string", name: "endnoteBody", label: "Closing note", ui: { component: "textarea" } },
        ],
      },
    ],
  },
});

import { defineConfig } from "tinacms";

export default defineConfig({
  branch: process.env.TINA_BRANCH || "main",
  clientId: process.env.NEXT_PUBLIC_TINA_CLIENT_ID,
  token: process.env.TINA_TOKEN,
  build: { outputFolder: "admin", publicFolder: "." },
  media: { tina: { mediaRoot: "media", publicFolder: "." } },
  schema: {
    collections: [
      {
        name: "post",
        label: "Journal Posts",
        path: "content/posts",
        format: "md",
        ui: { router: ({ document }) => `/blog/${document._sys.filename}` },
        fields: [
          { type: "string",   name: "title",       label: "Title", isTitle: true, required: true },
          { type: "datetime", name: "date",        label: "Date",  required: true },
          { type: "string",   name: "stage",       label: "Framework stage",
            options: ["Awaken","Understand","Reconnect","Become","Relate"] },
          { type: "string",   name: "excerpt",     label: "Short summary", ui: { component: "textarea" } },
          { type: "string",   name: "readingTime", label: "Reading time" },
          { type: "boolean",  name: "draft",       label: "Draft (hidden from site)" },
          { type: "rich-text",name: "body",        label: "Body", isBody: true }
        ]
      }
    ]
  }
});

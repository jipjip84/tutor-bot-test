# OC Connect (prototype)

A clickable prototype of OC Connect, an AI-first employee hub for Okanagan College. It is one HTML file with fictional example data.

The styling follows Okanagan College branding: OC red (cherry) for actions, Cabernet for headings and the sidebar, and Modern Era where it is installed (Hanken Grotesk otherwise). The colour hex values are approximations; replace the tokens at the top of `index.html` with the exact values from the brand guidelines.

- **Connect:** Home ("Needs you", who's out, events, AI catch-up), News (posts, required acknowledgements, kudos) and People (search by name, city or skill).
- **Me:** Time off (balances, booking with overlap warnings), Expenses (policy hints, receipt scanning) and Profile.
- **My team** (manager view): who's-out grid, members (add, edit, offboard), onboarding checklist, budget and Approvals.
- **Ask Connect:** an assistant you open with Ctrl/Cmd+K. It prepares actions as editable cards. Nothing is submitted until you press the button on the card.

Opened as a claude.ai artifact, the assistant uses Claude. Opened directly in a browser, it falls back to a built-in demo assistant that handles common requests. Data is saved in your browser; use "Reset example data" in the sidebar to start over.

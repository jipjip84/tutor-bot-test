# OC Connect (prototype)

A clickable prototype of OC Connect, an AI-first employee hub for Okanagan College. It is one HTML file with fictional example data.

The styling follows Okanagan College branding: OC red (cherry) for actions, Cabernet for headings and the sidebar, and Modern Era where it is installed (Hanken Grotesk otherwise). The colour hex values are approximations; replace the tokens at the top of `index.html` with the exact values from the brand guidelines.

- **Work queue:** four tabs. *Needs you* holds approvals, tickets waiting on your reply and policies to acknowledge. *Waiting on others* shows your pending requests, unpaid claims and open tickets, with who has each one and for how long. *Past* lists finished requests and resolved tickets. *Activity log* records everything, grouped by day. Use *New request* to open a ticket with IT, Facilities, People Ops or Finance.
- **Connect:** Home ("Needs you", who's out, events, AI catch-up), News (posts, required acknowledgements, kudos) and People (search by name, city or skill).
- **Me:** Time off (balances, booking with overlap warnings), Expenses (policy hints, receipt scanning) and Profile.
- **My team** (manager view): who's-out grid, members (add, edit, offboard), onboarding checklist, budget (approvals now live in the Work queue).
- **Ask Connect:** an assistant you open with Ctrl/Cmd+K. It prepares actions as editable cards. Nothing is submitted until you press the button on the card.

Opened as a claude.ai artifact, the assistant uses Claude. Opened directly in a browser, it falls back to a built-in demo assistant that handles common requests. Data is saved in your browser; use "Reset example data" in the sidebar to start over.

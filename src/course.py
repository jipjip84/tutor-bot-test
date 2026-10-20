"""Course content for Harvest Ledger.

Eight weeks, two textbook chapters per week. Mon/Tue cover the first
chapter, Wed/Thu the second, Fri mixes both. Each card is
(section, term, definition, farm example, illustration key).
"""

BOOK = "Principles of Management (LibreTexts)"

WEEKS = [
    {
        "title": "Breaking Ground",
        "chapters": "Ch 1–2",
        "build": "Red Barn",
        "days": [
            ("What managers do", "Ch 1", [
                ("1.1", "Management", "The art of getting things done through the efforts of other people. A manager's main challenge is solving problems creatively.", "The farm manager doesn't milk every cow. They make sure the milking gets done, and done well.", "barn"),
                ("1.5", "P-O-L-C framework", "The four management functions: planning, organizing, leading and controlling. Credited to Henri Fayol, and tightly linked in daily practice.", "Plan the crop, organize the crew, lead them through harvest, then check yield against target.", "almanac"),
                ("1.5", "Strategic, tactical, operational planning", "Strategic planning is long-range (3+ years) and organization-wide. Tactical planning (1–3 years) turns it into concrete means. Operational planning (under a year) sets the action steps.", "Strategic: go organic in five years. Tactical: convert the north fields over two seasons. Operational: spread compost on Tuesday.", "almanac"),
                ("1.5", "Controlling", "Keeping performance on standard in three steps: set performance standards, compare actual performance against them, and take corrective action when needed.", "Target 170 bushels an acre, measure 140, then fix the irrigation.", "chart"),
            ]),
            ("Managers, roles and the triple bottom line", "Ch 1", [
                ("1.3", "Line vs. staff manager", "A line manager runs a function that directly makes the product or service. A staff manager runs a supporting function such as finance or accounting.", "The harvest boss is line. The person keeping the farm's books is staff.", "hands"),
                ("1.3", "Mintzberg's 10 managerial roles", "Interpersonal (figurehead, leader, liaison), informational (monitor, disseminator, spokesperson) and decisional (entrepreneur, disturbance handler, resource allocator, negotiator).", "In one morning the farmer greets the county inspector, reads grain prices, and haggles with the seed dealer.", "vane"),
                ("1.6", "Triple bottom line", "Measuring business performance on social, environmental and economic results: people, planet, profit.", "A good year means fair wages for the crew, healthy soil, and money left over.", "scale"),
                ("1.7", "Organizational citizenship behaviors (OCBs)", "Voluntary extra-role behaviors that help the organization but aren't formally rewarded, such as helping, sportsmanship and civic virtue.", "The hand who stays late to chase loose calves back in, unasked.", "cow"),
            ]),
            ("Personality at work", "Ch 2", [
                ("2.3", "Big Five personality traits (OCEAN)", "Openness, conscientiousness, extraversion, agreeableness and neuroticism: five dimensions that explain much of how personalities differ.", "Every new seasonal picker brings a different mix of the five.", "hands"),
                ("2.3", "Conscientiousness", "Being organized, systematic, punctual, achievement-oriented and dependable. The one trait that predicts job performance across all occupations.", "The worker who checks every water trough twice, every day.", "water"),
                ("2.3", "Proactive personality", "An inclination to fix what's wrong, change things and take initiative rather than wait to be told.", "Spots a sagging fence post and resets it before the cattle find the gap.", "fence"),
                ("2.3", "Self-efficacy", "Belief that you can perform a specific task successfully. Unlike broad traits it is task-specific, and it predicts performance.", "Confident on the tractor, nervous with a chainsaw: self-efficacy is per task.", "tractor"),
            ]),
            ("Perception and attitudes", "Ch 2", [
                ("2.4", "Self-fulfilling prophecy", "When a stereotype leads you to act in a certain way, the other person responds in a way that confirms the stereotype.", "Treat the new hand as useless, give them only grunt work, and they never learn to drive the combine.", "scarecrow"),
                ("2.5", "Organizational justice", "Perceived fairness at work: procedural (fair processes), distributive (fair rewards) and interactional (being treated with dignity).", "Bonus rules everyone can see, split fairly, explained respectfully.", "scale"),
                ("2.5", "Psychological contract", "The unspoken understanding of what an employee will give the organization and what they'll get back.", "Work the long harvest weeks, and in return get a quiet winter and the farm's goodwill.", "basket"),
                ("2.6", "Person-organization vs. person-job fit", "P-O fit is how well your values and goals match the organization's. P-J fit is how well your skills (KSAOs) match the job's demands.", "A great mechanic (job fit) who hates early mornings may never fit a dairy (organization fit).", "barn"),
            ]),
            ("Bringing in the sheaves: Ch 1–2", "Ch 1–2", [
                ("1.4", "Entrepreneurship", "Recognizing opportunities (needs, wants, problems) and using or creating resources to launch innovative, well-planned ventures.", "Seeing city demand for microgreens and turning a spare shed into a grow room.", "seedling"),
                ("1.6", "Corporate social responsibility (CSR)", "Taking responsibility for your impact on customers, suppliers, employees, shareholders, communities and the environment, beyond what the law requires.", "Leaving a buffer strip along the creek even though no rule demands it.", "rain"),
                ("2.5", "Job satisfaction", "The feelings people have toward their job; probably the most studied and most important work attitude.", "The milker who loves the calm of the 5am barn.", "cow"),
                ("2.7", "Absenteeism and turnover", "Absenteeism is unscheduled absence; turnover is an employee leaving the organization. Both are costly.", "Losing two trained pickers mid-harvest costs more than their wages.", "basket"),
            ]),
        ],
    },
    {
        "title": "Reading the Old Almanac",
        "chapters": "Ch 3–4",
        "build": "Hen Yard",
        "days": [
            ("Classical roots of management", "Ch 3", [
                ("3.3", "Scientific management", "Frederick Taylor's approach: study work scientifically (time-and-motion studies) to find the one best way to do each task.", "Timing three ways to pick strawberries and teaching everyone the fastest one.", "gear"),
                ("3.3", "Administrative principles (Fayol)", "Henri Fayol's focus on the whole organization and the functions of management, with principles like unity of command, division of work and scalar chain.", "Each picker answers to one row boss, so orders never clash.", "almanac"),
                ("3.3", "Bureaucracy (Weber)", "Max Weber's ideal organization: clear division of labour, hierarchy, written rules, and hiring and promotion by merit.", "A big grain co-op grades every farmer's wheat by the same written standard.", "silo"),
                ("3.3", "Hawthorne studies", "Western Electric studies showing that social factors and management attention affect productivity. They launched the human relations movement.", "Milkers worked harder when the owner showed interest in them, not because of the new lights.", "cow"),
            ]),
            ("Modern views and global trends", "Ch 3", [
                ("3.3", "Theory X and Theory Y", "McGregor's two sets of assumptions. Theory X: workers dislike work and must be controlled. Theory Y: workers seek responsibility and direct themselves.", "A Theory Y farmer lets the crew design next year's crop rotation.", "hands"),
                ("3.3", "Contingency theory", "There is no one best way to manage. The right approach depends on the situation: environment, technology, size.", "Irrigation plans for a desert vineyard and a rainy dairy pasture can't be the same.", "rain"),
                ("3.3", "Systems theory", "The organization is an open system of related parts that takes inputs from its environment, transforms them, and produces outputs.", "Seed, water and labour go in; crops come out; soil health feeds back into next season.", "wheat"),
                ("3.5", "Outsourcing and offshoring", "Outsourcing contracts work to another company. Offshoring moves work to another country, inside the firm or through a foreign provider.", "Hiring a custom harvester instead of buying a combine is outsourcing.", "tractor"),
            ]),
            ("Mission, vision and values", "Ch 4", [
                ("4.3", "Mission", "An organization's basic reason to exist: what it does, for whom, and how. It describes purpose in the present.", "\"Pasture-raised beef for families in our valley.\"", "barn"),
                ("4.3", "Vision", "A future-facing statement of what the organization hopes to become. It should inspire and give direction.", "\"In ten years, every school lunch in the county uses our produce.\"", "sun"),
                ("4.3", "Big hairy audacious goal (BHAG)", "Collins and Porras's term for a bold, long-term goal that energizes and focuses an organization.", "Becoming the first carbon-negative dairy in the state.", "apple"),
                ("4.5", "Four types of creativity", "Imitation, variation, combination and transformation: increasingly novel ways to generate ideas.", "Copy a neighbour's farm stand, tweak it, add a pick-your-own patch, then reinvent it as a farm-stay.", "seedling"),
            ]),
            ("Stakeholders", "Ch 4", [
                ("4.6", "Stakeholders", "Individuals or groups who affect or are affected by the organization: employees, customers, suppliers, investors, communities.", "Neighbours downstream of your runoff are stakeholders too.", "hands"),
                ("4.6", "Stakeholder analysis", "Identifying stakeholders and assessing their interests and influence so their expectations shape mission, vision and strategy.", "Mapping who cares about your new hog barn: buyers, neighbours, the water board.", "pig"),
                ("4.6", "Stakeholder power, legitimacy, urgency", "Three attributes for judging how much a stakeholder matters: ability to influence the firm, how appropriate their claim is, and how time-sensitive it is.", "The county regulator has power and legitimacy; a flood warning adds urgency.", "vane"),
                ("4.6", "Primary vs. secondary stakeholders", "Primary stakeholders have a direct stake (employees, customers, owners). Secondary ones are indirectly affected (media, activists).", "Your grain buyer is primary; the local paper covering farm runoff is secondary.", "market"),
            ]),
            ("Bringing in the sheaves: Ch 3–4", "Ch 3–4", [
                ("3.6", "Hofstede's cultural dimensions", "Ways national cultures differ: individualism/collectivism, power distance, uncertainty avoidance, masculinity/femininity, long-term orientation.", "In a collective village, the co-op decides together when to start harvest.", "hands"),
                ("3.6", "Power distance", "How much a society accepts that power is unequally distributed in institutions and organizations.", "On some estates nobody questions the owner; on others the crew argues every call.", "scale"),
                ("4.3", "Organizational values", "Shared principles and beliefs that guide behavior and decisions, often stated next to mission and vision.", "\"We never leave a gate open\" is a value everyone lives by.", "fence"),
                ("4.7", "Crafting mission and vision statements", "Good statements are short, clear, memorable and inspiring, built with stakeholder input and shared across the organization.", "Short enough to paint on the side of the barn.", "barn"),
            ]),
        ],
    },
    {
        "title": "Planning the Planting",
        "chapters": "Ch 5–6",
        "build": "Tractor",
        "days": [
            ("How strategies emerge", "Ch 5", [
                ("5.3", "Strategy formulation vs. implementation", "Formulation is choosing the strategy. Implementation is the actions and resources that put it into practice.", "Deciding to sell direct to restaurants vs. actually building the delivery route.", "tractor"),
                ("5.4", "Intended strategy", "The strategy leaders plan and deliberately set out to pursue.", "The winter plan: 200 acres of corn.", "almanac"),
                ("5.4", "Emergent strategy", "A strategy that arises unplanned, from a pattern of responses to unexpected opportunities and threats (Mintzberg).", "Drought kills the corn, sunflowers thrive, and you quietly become a sunflower farm.", "sun"),
                ("5.4", "Realized strategy", "The strategy actually followed: the parts of the intended strategy that happened plus the emergent strategy.", "Half corn as planned, half sunflowers by accident: that's what you really did.", "wheat"),
            ]),
            ("Looking inside: resources and the value chain", "Ch 5", [
                ("5.5", "Strategy as trade-offs", "Porter's view that strategy means choosing what not to do. Trade-offs, discipline and focus build a unique position that's hard to copy.", "Saying no to commodity milk so you can focus on artisan cheese.", "scale"),
                ("5.5", "Competitive advantage", "The ability to create more value or perform better than rivals, in a sustainable way.", "The only orchard in the region with a frost-proof heritage apple.", "apple"),
                ("5.6", "VRIO/VRIS framework", "A resource gives sustained advantage if it is valuable, rare, hard to imitate, and not easily substituted.", "Rich river-bottom soil: valuable, rare, impossible to copy.", "seedling"),
                ("5.6", "Value chain", "The primary and support activities through which a firm creates value. Used to find where cost or differentiation advantages come from.", "Seed, grow, harvest, pack, truck, sell, plus the books and repairs that support it all.", "market"),
            ]),
            ("Looking outside and the strategy diamond", "Ch 5", [
                ("5.7", "PESTEL analysis", "Examines the general environment's political, economic, social, technological, environmental and legal factors.", "Farm subsidies, interest rates, plant-based diets, drones, drought, labour law.", "vane"),
                ("5.7", "Porter's five forces", "Industry analysis of rivalry, threat of new entrants, threat of substitutes, buyer power and supplier power.", "Three supermarket chains buy all the milk: buyer power squeezes the price.", "market"),
                ("5.8", "Strategy diamond", "Hambrick and Fredrickson's five elements of a coherent strategy: arenas, vehicles, differentiators, staging and pacing, economic logic.", "Where we farm, how we expand, why buyers pick us, in what order, and how we make money.", "almanac"),
                ("5.8", "Arenas and vehicles", "Arenas are where the firm is active (products, markets, geographies). Vehicles are how it gets there (internal growth, alliances, acquisitions).", "Arena: farmers' markets in three towns. Vehicle: partnering with a local bakery.", "tractor"),
            ]),
            ("Goals and objectives", "Ch 6", [
                ("6.3", "Goals vs. objectives", "Goals are broad, longer-term outcome statements. Objectives are specific, measurable, time-bound targets that support them.", "Goal: become known for great eggs. Objective: 95% grade-A eggs by June.", "chicken"),
                ("6.3", "Hierarchy of goals", "Goals cascade from mission and strategy down to units, departments and individuals so everything lines up.", "Farm goal, then dairy-barn goal, then each milker's daily target.", "silo"),
                ("6.4", "Management by objectives (MBO)", "Drucker's process: managers and employees set objectives together, review progress, and reward based on results.", "The herd manager and owner agree to cut calf losses to 3% this year.", "cow"),
                ("6.5", "Goal-setting theory", "Locke and Latham: specific, difficult goals with feedback lead to higher performance than vague or easy goals.", "\"Pick 40 crates by noon\" beats \"do your best\".", "basket"),
            ]),
            ("Bringing in the sheaves: Ch 5–6", "Ch 5–6", [
                ("5.7", "SWOT analysis", "A summary of internal strengths and weaknesses and external opportunities and threats.", "Strength: fertile soil. Threat: a new mega-farm in the next county.", "scarecrow"),
                ("5.8", "Differentiators and economic logic", "Differentiators are how the firm wins in its arenas. Economic logic is how it earns returns, such as lowest cost or premium prices.", "Heritage pork chefs love (differentiator), sold at a premium (economic logic).", "pig"),
                ("6.4", "Balanced scorecard", "Kaplan and Norton's framework measuring financial, customer, internal process, and learning and growth perspectives.", "Profit per acre, buyer happiness, harvest speed, and crew skills, side by side.", "chart"),
                ("6.6", "360-degree feedback", "Appraisal using input from supervisors, peers, subordinates and sometimes customers, plus self-assessment.", "The foreman hears from the owner, the crew, and the chefs who buy the produce.", "hands"),
            ]),
        ],
    },
    {
        "title": "Raising the Barn",
        "chapters": "Ch 7–8",
        "build": "Grain Silo",
        "days": [
            ("Building the structure", "Ch 7", [
                ("7.3", "Organizational structure", "How an organization's activities are divided, coordinated and controlled, including who reports to whom.", "Who drives, who hauls, who runs the dryer, and who they all answer to.", "barn"),
                ("7.3", "Formalization", "How far policies, procedures, job descriptions and rules are written down and spelled out.", "A laminated step-by-step milking hygiene checklist on the parlour wall.", "almanac"),
                ("7.3", "Centralization", "How much decision-making authority sits at the top of the organization.", "Only the owner can decide when to start harvest: highly centralized.", "vane"),
                ("7.3", "Hierarchical levels and span of control", "How many layers the structure has (tall vs. flat) and how many people report to one manager.", "One supervisor can handle 20 experienced pickers but only five new tractor drivers.", "hands"),
            ]),
            ("Shapes of organizations", "Ch 7", [
                ("7.3", "Mechanistic vs. organic structures", "Mechanistic: bureaucratic, centralized, formalized. Organic: flexible, decentralized, suited to changing environments.", "A big poultry plant vs. a start-up vertical farm.", "gear"),
                ("7.3", "Functional vs. divisional structure", "Functional groups people by function (marketing, finance, operations). Divisional sets up self-contained units by product, customer or region.", "One farm with a crops team and a sales team, vs. separate dairy and orchard divisions.", "silo"),
                ("7.4", "Matrix structure", "Combines functional and product or project lines so employees report to two managers.", "An agronomist reports to the crops manager and the new organic-conversion project lead.", "fence"),
                ("7.4", "Boundaryless organization", "A structure that removes barriers between departments and with outside partners, often using temporary teams and networks.", "Neighbouring farms share one combine crew and swap labour at harvest.", "tractor"),
            ]),
            ("Managing change", "Ch 7", [
                ("7.5", "Resistance to change", "Reluctance to support change, from disrupted habits, personality, uncertainty, fear of failure or personal impact.", "\"We've always cut hay in June\" when switching to a new rotation.", "scarecrow"),
                ("7.6", "Lewin's three-stage model", "Unfreeze current behaviors, change to new ones, then refreeze so the new behaviors stick.", "Show the crew why no-till matters, switch the drills, then make no-till the standard.", "rain"),
                ("7.6", "Force field analysis", "Lewin's tool listing the forces driving change and the forces resisting it, so managers can strengthen one and weaken the other.", "Drivers: soil savings, subsidies. Resisters: old equipment, habit.", "scale"),
                ("7.6", "Change agent", "The person who starts and manages a change effort, from inside or outside the organization.", "The young farmer back from ag college pushing for precision irrigation.", "seedling"),
            ]),
            ("Organizational culture", "Ch 8", [
                ("8.3", "Organizational culture", "Shared assumptions, values and beliefs that show people what behavior is appropriate in the organization.", "Nobody wrote it down, but everyone knows you help a neighbour bring in hay before rain.", "barn"),
                ("8.3", "Levels of culture", "Schein's three layers: deep assumptions, espoused values and visible artifacts.", "The stewardship belief underneath, the \"care for the land\" motto, the old tractor kept polished by the gate.", "apple"),
                ("8.4", "Strong culture", "Values that are widely shared and intensely held. A strong culture guides behavior and can help performance or block change.", "A family farm where every generation lives the same stewardship ethic.", "house"),
                ("8.4", "Subcultures and countercultures", "Subcultures share values within a subgroup. Countercultures hold values that directly oppose the dominant culture.", "The night-calving crew has its own rhythms; the crew that skips biosecurity rules is a counterculture.", "cow"),
            ]),
            ("Bringing in the sheaves: Ch 7–8", "Ch 7–8", [
                ("7.3", "Departmentalization", "Grouping jobs into departments by function, product, geography or customer.", "Crops, livestock and the farm shop, each its own department.", "market"),
                ("8.5", "Attraction-selection-attrition (ASA)", "Culture persists because people who fit are attracted, selected and retained, while poor fits leave.", "People who love early mornings apply to the dairy, and the night owls drift away.", "sun"),
                ("8.5", "Onboarding (organizational socialization)", "How new employees learn the attitudes, knowledge, skills and behaviors needed to function in the organization.", "Day one: the safety walk around the bull pen and the harvest-supper tradition.", "hands"),
                ("8.5", "Rituals, stories and symbols", "Cultural carriers that transmit values: ceremonies, legendary stories, logos, physical layout.", "The story of grandpa saving the herd in the '78 blizzard, told every winter.", "almanac"),
            ]),
        ],
    },
    {
        "title": "Neighbours and Foremen",
        "chapters": "Ch 9–10",
        "build": "Dairy Herd",
        "days": [
            ("The language of networks", "Ch 9", [
                ("9.3", "Social network analysis (SNA)", "Mapping and measuring relationships and flows among people or groups to see how work and information really move.", "Drawing who calls whom when a cow gets sick reveals the real chain of help.", "vane"),
                ("9.3", "Nodes and ties", "Nodes are the people or units in a network. Ties are the relationships linking them.", "Farms are nodes; shared equipment and phone calls are ties.", "fence"),
                ("9.3", "Centrality", "How connected a person is, or how central they are to information flows in a network.", "The feed-store owner who knows every farmer in the county.", "market"),
                ("9.3", "Strong vs. weak ties", "Strong ties are close, frequent relationships. Weak ties are casual acquaintances, and they often bring new information.", "Your brother helps every harvest (strong); a fair acquaintance tells you about a new grain buyer (weak).", "hands"),
            ]),
            ("Bridges and social capital", "Ch 9", [
                ("9.3", "Structural holes", "Gaps between unconnected groups in a network. Whoever bridges them gains information and control.", "The organic growers and the restaurant owners don't know each other yet.", "fence"),
                ("9.3", "Brokers (bridges)", "People who connect groups that otherwise aren't connected and control the information flowing between them.", "The farmers' market manager who introduces growers to chefs.", "market"),
                ("9.4", "Social capital", "The value a person or organization gets from its network of relationships.", "When your barn burns, twenty neighbours show up with hammers.", "barn"),
                ("9.6", "Personal, operational, strategic networks", "Personal: contacts outside work for development. Operational: people needed to get today's work done. Strategic: relationships that help with future priorities.", "Ag-college friends, your vet and mechanic, and the co-op board you want to join.", "hands"),
            ]),
            ("Who leads? Traits and behaviors", "Ch 10", [
                ("10.3", "Trait approaches to leadership", "Studying characteristics like intelligence, Big Five traits, self-esteem and integrity that relate to who emerges as leader and who leads well.", "The crew naturally follows the calm, honest one when the storm hits.", "sun"),
                ("10.4", "Task-oriented (initiating structure)", "Leader behaviors that structure work: setting goals, clarifying expectations, monitoring performance.", "\"North field by 3pm, two trucks, check moisture every load.\"", "chart"),
                ("10.4", "People-oriented (consideration)", "Leader behaviors showing concern for employees' feelings and well-being and treating them with respect.", "The foreman who brings cold drinks and asks about your sick kid.", "hands"),
                ("10.4", "Authoritarian, democratic, laissez-faire", "Decision styles: deciding alone, involving employees, or leaving decisions to employees.", "Owner decides, crew votes, or \"you figure it out\".", "scale"),
            ]),
            ("Leadership depends on the field", "Ch 10", [
                ("10.5", "Fiedler's contingency theory", "Leader effectiveness depends on matching style (measured by LPC) to how favorable the situation is: leader-member relations, task structure, position power.", "A task-driven boss shines in a harvest emergency; a relationship-builder shines in a slow season.", "rain"),
                ("10.5", "Situational leadership theory", "Hersey and Blanchard: leaders adapt their style (telling, selling, participating, delegating) to followers' readiness.", "Tell the new hand exactly how to hitch the trailer; delegate to the 20-year veteran.", "tractor"),
                ("10.5", "Path-goal theory", "Leaders clarify the path to goals using directive, supportive, participative or achievement-oriented behavior suited to the employee and setting.", "Clearing the muddy lane so the trucks can actually reach the field.", "fence"),
                ("10.6", "Transformational leadership", "Inspiring followers to exceed expectations through charisma, inspirational motivation, intellectual stimulation and individualized consideration.", "The farmer whose vision of a regenerative valley gets the whole crew excited.", "sun"),
            ]),
            ("Bringing in the sheaves: Ch 9–10", "Ch 9–10", [
                ("9.3", "Small-world (six degrees)", "Most people are linked to anyone else through a short chain of acquaintances.", "Your vet's cousin knows the buyer at the big grocery chain.", "vane"),
                ("10.6", "Transactional leadership", "Leadership based on exchanges, using contingent rewards and management by exception.", "Bonus per crate picked, and the boss only steps in when something goes wrong.", "basket"),
                ("10.6", "Leader-member exchange (LMX)", "Leaders form relationships of different quality with each follower. High-quality exchanges bring trust, support and better results.", "The foreman's trusted inner circle gets the best fields and the most coaching.", "hands"),
                ("10.6", "Servant leadership", "Leaders who put employees' needs first, help them grow and succeed, and act ethically.", "The owner who mucks stalls alongside the crew and pays for their certifications.", "barn"),
            ]),
        ],
    },
    {
        "title": "Weather Calls and Fence Talk",
        "chapters": "Ch 11–12",
        "build": "Beehives",
        "days": [
            ("How decisions get made", "Ch 11", [
                ("11.3", "Programmed vs. nonprogrammed decisions", "Programmed decisions are routine and handled by rules. Nonprogrammed decisions are new and unstructured.", "\"Reorder diesel at 25%\" vs. responding to a brand-new livestock disease.", "water"),
                ("11.3", "Rational decision-making model", "Identify the problem, set and weight criteria, generate and evaluate alternatives, choose the best, implement, evaluate.", "Choosing a new tractor: price, horsepower, dealer support, scored and compared.", "tractor"),
                ("11.3", "Bounded rationality", "Decision makers are limited by time, information and mental capacity, so they can't be fully rational.", "Nobody knows next year's rainfall, so you plant on your best guess.", "rain"),
                ("11.3", "Satisficing", "Accepting the first option that meets minimum criteria instead of hunting for the best one.", "Buying the first decent used baler at a fair price instead of checking every auction in the state.", "wheat"),
            ]),
            ("When decisions go wrong", "Ch 11", [
                ("11.4", "Overconfidence bias", "Overestimating how accurate your judgments and abilities are.", "\"I can get all 300 acres in before the rain.\" You can't.", "rain"),
                ("11.4", "Anchoring", "Leaning too heavily on the first piece of information you get when making a judgment.", "The first bid for your calves sets the bar for every offer after.", "cow"),
                ("11.4", "Framing bias", "Being swayed by how information is presented, such as gains vs. losses.", "\"90% germination\" sounds better than \"10% of seeds fail\".", "seedling"),
                ("11.4", "Escalation of commitment", "Continuing to invest in a failing course of action because of what you've already put in.", "Replanting a failed crop for the third season because \"we've sunk so much in\".", "scarecrow"),
            ]),
            ("Deciding as a group", "Ch 11", [
                ("11.5", "Groupthink", "A group avoids critically evaluating ideas to keep the peace and consensus, which leads to poor decisions.", "Nobody says the new hog barn is in the flood plain because everyone's excited.", "pig"),
                ("11.5", "Nominal group technique", "Members generate ideas alone, share them in turn, discuss, then vote privately to reduce pressure to conform.", "Each crew member writes their idea for fixing the bottleneck before anyone talks.", "almanac"),
                ("11.5", "Delphi technique", "Experts give anonymous written input over several rounds, with feedback, until they reach consensus.", "Agronomists email anonymous yield forecasts until the numbers converge.", "chart"),
                ("11.3", "Intuitive decision making", "Reaching decisions quickly by recognizing patterns from experience rather than by conscious analysis.", "An old farmer smells rain coming and moves the hay in.", "vane"),
            ]),
            ("How messages travel", "Ch 12", [
                ("12.3", "Communication process model", "A sender encodes a message and sends it through a channel. The receiver decodes it and gives feedback. Noise can distort it.", "You shout \"gate!\" across the yard; the hand hears \"wait!\" over the tractor.", "vane"),
                ("12.3", "Noise", "Anything that interferes with or distorts a message between sender and receiver.", "A roaring grain dryer next to the person giving instructions.", "gear"),
                ("12.4", "Filtering", "Distorting or holding back information to manage how someone will react.", "Telling the owner the harvest is \"going fine\" while skipping the broken auger.", "silo"),
                ("12.4", "Information overload", "Receiving more information than you can process, so messages get missed or misunderstood.", "Forty texts about weather, prices and parts before 7am.", "almanac"),
            ]),
            ("Bringing in the sheaves: Ch 11–12", "Ch 11–12", [
                ("11.5", "Brainstorming", "A group generates as many ideas as possible without criticism, building on each other's.", "Twenty ideas for the empty barn, from goat yoga to a cider press.", "barn"),
                ("12.4", "Grapevine (workplace gossip)", "The informal channel through which rumors and unofficial information spread.", "Everyone knew about the sale of the north farm before the owner said a word.", "hands"),
                ("12.6", "Channel richness", "How much information a channel can carry. Face-to-face is richest; impersonal written messages are leanest.", "Tell a worker they're being let go face to face, not on a note in the tool shed.", "house"),
                ("12.7", "Active listening", "Listening with attention, paraphrasing, asking questions and responding to show you understand.", "\"So the heifers are off feed since Tuesday? What changed?\"", "cow"),
            ]),
        ],
    },
    {
        "title": "Harvest Crew Spirit",
        "chapters": "Ch 13–14",
        "build": "Apple Orchard",
        "days": [
            ("How groups grow", "Ch 13", [
                ("13.3", "Tuckman's stages of development", "Groups move through forming, storming, norming, performing and adjourning.", "The seasonal crew squabbles in week one, finds its rhythm by week three, and parties at the end.", "hands"),
                ("13.3", "Punctuated equilibrium", "Groups alternate between long stretches of inertia and bursts of change, often around a project's midpoint.", "The crew coasts until mid-season, then suddenly reorganizes the whole picking system.", "apple"),
                ("13.3", "Group cohesion", "How attracted members are to the group and how motivated they are to stay in it.", "The crew that eats lunch together under the same oak every day.", "apple"),
                ("13.3", "Team norms", "Shared expectations about how members should behave.", "On this crew, nobody leaves until the last crate is loaded.", "basket"),
            ]),
            ("Designing teams", "Ch 13", [
                ("13.4", "Task interdependence", "How much members depend on each other: pooled, sequential or reciprocal.", "Pooled: pickers in separate rows. Sequential: picker, packer, trucker. Reciprocal: combine and grain cart working together.", "tractor"),
                ("13.4", "Task roles vs. social roles", "Task roles help the team get work done. Social (maintenance) roles keep relationships healthy.", "One person keeps the tally; another keeps everyone laughing in the heat.", "sun"),
                ("13.5", "Self-managed teams", "Teams with no formal supervisor that plan and control their own work.", "The orchard crew sets its own schedule and divides the blocks.", "apple"),
                ("13.5", "Cross-functional teams", "Teams with members from different functions working toward one goal.", "Agronomist, mechanic and marketer planning the new pumpkin patch together.", "market"),
            ]),
            ("What holds teams back", "Ch 13", [
                ("13.6", "Social loafing", "Putting in less effort when working in a group than when working alone.", "Six people \"moving\" hay bales while two do all the lifting.", "wheat"),
                ("13.6", "Lack of trust", "A barrier to team effectiveness. Without trust, members hold back information and effort.", "Pickers hide the good rows from each other when they don't trust the bonus split.", "fence"),
                ("13.6", "Collective efficacy", "A team's shared belief that it can successfully accomplish its tasks.", "\"We brought in 400 acres last year. We can do this.\"", "basket"),
                ("13.4", "Virtual teams", "Teams whose members are spread out and work together mainly through technology.", "Farmers in three states sharing data on a drought-resistant seed trial.", "chart"),
            ]),
            ("What drives people: needs", "Ch 14", [
                ("14.3", "Maslow's hierarchy of needs", "Physiological, safety, social, esteem, self-actualization. Lower needs must be met before higher ones motivate.", "Fair wages and housing come before pride in a prize-winning crop.", "barn"),
                ("14.3", "ERG theory", "Alderfer's needs of existence, relatedness and growth. Several can operate at once, and frustration can cause regression.", "A worker blocked from growing into a lead role starts caring more about pay.", "seedling"),
                ("14.3", "Herzberg's two-factor theory", "Hygiene factors (pay, security, conditions) prevent dissatisfaction. Motivators (achievement, recognition, responsibility) create satisfaction.", "A new barn roof stops complaints; a blue ribbon at the fair motivates.", "ribbon"),
                ("14.3", "McClelland's acquired needs", "People are driven by needs for achievement, affiliation and power, learned through life experience.", "One hand wants the top yield, another wants friends, another wants to run the crew.", "hands"),
            ]),
            ("Bringing in the sheaves: Ch 13–14", "Ch 13–14", [
                ("14.4", "Equity theory", "People compare their input/outcome ratio with a referent's. Feeling under- or over-rewarded pushes them to restore balance.", "A picker learns the new hire earns more for the same rows, and their effort drops.", "scale"),
                ("14.4", "Expectancy theory", "Vroom: motivation depends on expectancy (effort leads to performance), instrumentality (performance leads to reward) and valence (value of the reward).", "A bonus nobody believes they can reach motivates nobody.", "basket"),
                ("14.4", "Reinforcement theory", "Behavior is shaped by its consequences: positive and negative reinforcement increase it; punishment and extinction decrease it.", "Praise every time the gate gets latched, and soon it always does.", "fence"),
                ("14.5", "Intrinsic vs. extrinsic motivation", "Intrinsic motivation comes from the work itself. Extrinsic motivation comes from outside rewards such as pay.", "Loving the smell of turned soil vs. working for the harvest bonus.", "seedling"),
            ]),
        ],
    },
    {
        "title": "Weighing the Harvest",
        "chapters": "Ch 15–16",
        "build": "Farmhouse and Blue Ribbon",
        "days": [
            ("The essentials of control", "Ch 15", [
                ("15.3", "Control process", "Set standards, measure actual performance, compare it with the standards, and take corrective action.", "Standard: 30 litres per cow. Measure. Compare. Change the feed ration.", "cow"),
                ("15.4", "Feedforward control", "Control that heads off problems before an activity starts, such as inspecting inputs.", "Testing seed germination before planting.", "seedling"),
                ("15.4", "Concurrent control", "Control while an activity is in progress.", "The foreman walking the rows during harvest, checking fruit quality.", "apple"),
                ("15.4", "Feedback control", "Control after an activity ends, comparing outcomes with standards.", "Reviewing yield maps after harvest to plan next year.", "chart"),
            ]),
            ("Levels and money", "Ch 15", [
                ("15.4", "Bureaucratic vs. clan control", "Bureaucratic control uses rules, hierarchy and procedures. Clan control relies on shared values and culture.", "A rulebook on spraying vs. a crew that just cares about clean water.", "almanac"),
                ("15.5", "Budget", "A financial plan that allocates resources, used to compare actual spending and revenue against plan.", "$40,000 for fertilizer this season; check the receipts monthly.", "scale"),
                ("15.5", "Financial statements", "The income statement, balance sheet and cash flow statement used to monitor financial performance.", "Profit for the season, what the farm owns and owes, and whether cash lasts until harvest pays out.", "chart"),
                ("15.5", "Financial ratio analysis", "Liquidity, leverage, profitability and activity ratios used to judge financial health and compare performance.", "Can you pay this month's feed bill, and how much of the land does the bank own?", "chart"),
            ]),
            ("Nonfinancial and lean control", "Ch 15", [
                ("15.6", "Nonfinancial controls", "Controls based on measures like quality, customer satisfaction and employee behavior rather than money.", "Chef complaints about bruised tomatoes, tracked every week.", "market"),
                ("15.6", "Six Sigma", "A quality approach aiming for near-zero defects (3.4 per million) through measurement and process improvement.", "Driving cracked eggs down toward almost none.", "chicken"),
                ("15.7", "Lean production and kaizen", "Lean eliminates waste and improves every process continuously (from the Toyota Production System). Kaizen is small, constant improvement by everyone.", "Moving the wash station next to the packing shed saves 400 steps a day.", "gear"),
                ("15.7", "Just-in-time (JIT)", "Inventory arrives exactly when production needs it, keeping inventory costs low.", "Feed delivered weekly instead of filling (and spoiling) a giant silo.", "silo"),
            ]),
            ("Strategic human resource management", "Ch 16", [
                ("16.3", "Strategic HRM", "Aligning HR practices with strategy so that how you manage people supports competitive advantage.", "If you compete on artisan cheese, hire and train for craft, not speed.", "hands"),
                ("16.3", "Human capital", "Employees' knowledge, skills, abilities and experience that create value.", "The herd manager who can spot mastitis from across the barn.", "cow"),
                ("16.4", "War for talent", "Intense competition among organizations to attract and keep the best employees.", "Every farm in the valley wants the same three skilled mechanics.", "tractor"),
                ("16.5", "Structured interviews", "Every applicant gets the same job-related questions and is rated on the same criteria. More valid than unstructured interviews.", "Each applicant is asked how they'd handle a calving at 2am, and scored the same way.", "almanac"),
            ]),
            ("Bringing in the sheaves: Ch 15–16", "Ch 15–16", [
                ("15.8", "Personal balanced scorecard", "Applying the balanced scorecard to yourself: goals and measures across several life and career areas.", "Your own scorecard: grades, health, skills, and time on the farm.", "ribbon"),
                ("16.5", "Realistic job preview", "Giving applicants honest positive and negative information about the job, which reduces turnover.", "\"You'll love the sunrises. You'll also shovel manure in January.\"", "house"),
                ("16.6", "Pay for performance", "Linking pay to individual, group or organizational results: merit pay, bonuses, gainsharing, profit sharing, stock options.", "A bonus per pound of honey for the beekeepers.", "beehive"),
                ("16.7", "High-performance work system (HPWS)", "A bundle of HR practices (selective hiring, training, empowerment, performance-based pay) that together lift performance.", "Hire carefully, train well, let crews decide, share the profits: a farm that runs itself.", "barn"),
            ]),
        ],
    },
]

CHAPTER_TITLES = {
    1: "Introduction to Principles of Management",
    2: "Personality, Attitudes, and Work Behaviors",
    3: "History, Globalization, and Values-Based Leadership",
    4: "Developing Mission, Vision, and Values",
    5: "Strategizing",
    6: "Goals and Objectives",
    7: "Organizational Structure and Change",
    8: "Organizational Culture",
    9: "Social Networks",
    10: "Leading People and Organizations",
    11: "Decision Making",
    12: "Communication in Organizations",
    13: "Managing Groups and Teams",
    14: "Motivating Employees",
    15: "The Essentials of Control",
    16: "Strategic Human Resource Management",
}

# Farm scenarios per week: (situation, the card term that fits, why).
SCENARIOS = [
    [
        ("Your harvest boss's crew brings in the crop. Your bookkeeper's work supports it but never touches a plant. What describes the difference between their two roles?", "Line vs. staff manager", "The harvest boss contributes directly to the product (line); the bookkeeper provides supporting inputs (staff)."),
        ("A new hire was told the job came with housing and winter work. In spring the owner drops both, and the hire feels betrayed even though nothing was written down.", "Psychological contract", "The unwritten understanding of what each side gives and gets was broken."),
        ("Your annual report shows profit, soil health and how well the crew is paid, side by side.", "Triple bottom line", "People, planet and profit are measured together."),
    ],
    [
        ("Your co-op grades every grower's wheat with the same written rules and promotes inspectors only on test scores.", "Bureaucracy (Weber)", "Written rules, impersonal treatment and merit-based promotion are Weber's ideal bureaucracy."),
        ("The owner is sure the crew will slack off unless someone watches them every minute.", "Theory X and Theory Y", "That's a Theory X assumption: workers dislike work and must be controlled."),
        ("Before building a hog barn, you list the neighbours, the water board and your buyers, and rate how much each could affect the project.", "Stakeholder analysis", "Identifying stakeholders and weighing their interests and influence."),
    ],
    [
        ("You planned 200 acres of corn. A drought pushed you into sunflowers, and sunflowers became your main crop.", "Emergent strategy", "The strategy arose from responding to an unexpected event, not from the plan."),
        ("Your river-bottom soil is valuable, rare and impossible for any rival to copy.", "VRIO/VRIS framework", "A resource that passes these tests can give a sustained advantage."),
        ("Instead of saying \"pick faster\", you set \"40 crates by noon\" and post the tally every hour.", "Goal-setting theory", "Specific, difficult goals with feedback raise performance."),
    ],
    [
        ("Your agronomist answers to both the crops manager and the organic-conversion project lead.", "Matrix structure", "Reporting to two managers, one functional and one project, is a matrix."),
        ("Older hands keep saying \"we've always cut hay in June\" and drag their feet on the new rotation.", "Resistance to change", "Habit and uncertainty make people reluctant to support change."),
        ("People who love dawn milking apply, get hired and stay. Night owls quit within months.", "Attraction-selection-attrition (ASA)", "Culture sustains itself as fitting people are attracted and kept while poor fits leave."),
    ],
    [
        ("The farmers' market manager introduces organic growers to restaurant chefs who had never met.", "Brokers (bridges)", "They connect two otherwise unconnected groups."),
        ("You give a brand-new hand step-by-step instructions, but simply hand the keys to your 20-year veteran.", "Situational leadership theory", "Leadership style matched to each follower's readiness."),
        ("The crew lead pays a bonus per crate and only steps in when something goes wrong.", "Transactional leadership", "Contingent rewards plus management by exception."),
    ],
    [
        ("You've replanted the failed field three seasons running because you've \"already sunk so much in\".", "Escalation of commitment", "Continuing a failing course because of past investment."),
        ("The first offer for your calves was low, and you judge every later offer against it.", "Anchoring", "The first number became the reference point."),
        ("Your foreman says harvest is \"going fine\" and leaves out the broken auger.", "Filtering", "Information was held back to manage your reaction."),
    ],
    [
        ("Six people are assigned to stack hay bales, but two of them do nearly all the lifting.", "Social loafing", "People put in less effort in a group than alone."),
        ("A picker finds out a new hire earns more for the same rows, and starts slowing down.", "Equity theory", "An unfavourable comparison with a referent pushes the picker to rebalance by cutting effort."),
        ("Fixing the leaky barn roof stopped the complaints, but it took the county fair ribbon to get the crew excited.", "Herzberg's two-factor theory", "The roof is a hygiene factor; the ribbon (recognition) is a motivator."),
    ],
    [
        ("You test seed germination before planting, so a bad batch never goes in the ground.", "Feedforward control", "It heads off a problem before the activity starts."),
        ("Moving the wash station next to the packing shed saves the crew 400 steps a day.", "Lean production and kaizen", "Small continuous improvements that remove waste."),
        ("You tell applicants about shovelling manure in January as well as about the sunrises.", "Realistic job preview", "Honest good-and-bad information reduces later turnover."),
    ],
]

# The P-O-L-C sorting game: farm tasks and the function each belongs to.
POLC_ITEMS = [
    ("Deciding in winter which fields get corn next spring", "Planning"),
    ("Setting a target of 95% grade-A eggs by June", "Planning"),
    ("Mapping out a five-year move to organic", "Planning"),
    ("Assigning two people to the planter and one to irrigation", "Organizing"),
    ("Drawing up who reports to the harvest boss", "Organizing"),
    ("Setting up a separate team for the farm shop", "Organizing"),
    ("Rallying the tired crew before the last field", "Leading"),
    ("Coaching a new hand through their first calving", "Leading"),
    ("Explaining to the crew why the new rotation matters", "Leading"),
    ("Comparing yield per acre against the target", "Controlling"),
    ("Checking feed spending against the budget", "Controlling"),
    ("Inspecting packed crates for bruised fruit", "Controlling"),
]


def build():
    weeks = []
    for w, wk in enumerate(WEEKS, start=1):
        days = []
        for d, (title, chapter, cards) in enumerate(wk["days"], start=1):
            out = []
            for k, (section, term, definition, farm, art) in enumerate(cards, start=1):
                out.append({
                    "id": f"W{w}D{d}-{k}",
                    "section": section,
                    "term": term,
                    "definition": definition,
                    "farm": farm,
                    "art": art,
                })
            sections = sorted({c["section"] for c in out}, key=lambda s: [int(x) for x in s.split(".")])
            days.append({"title": title, "chapter": chapter, "sections": sections, "cards": out})
        terms = {c["term"] for d in days for c in d["cards"]}
        scenarios = []
        for q, answer, why in SCENARIOS[w - 1]:
            assert answer in terms, f"scenario answer not a week {w} card: {answer}"
            scenarios.append({"q": q, "answer": answer, "why": why})
        chapter_nums = sorted({int(c["section"].split(".")[0]) for d in days for c in d["cards"]})
        weeks.append({
            "title": wk["title"], "chapters": wk["chapters"], "build": wk["build"], "days": days,
            "chapterNames": [{"num": n, "title": CHAPTER_TITLES[n]} for n in chapter_nums],
            "scenarios": scenarios,
        })
    return {"book": BOOK, "weeks": weeks, "polc": [{"text": t, "fn": f} for t, f in POLC_ITEMS]}

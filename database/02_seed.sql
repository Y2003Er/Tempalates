-- Seed demo data
INSERT INTO organizations (id, slug, name) VALUES ('00000000-0000-0000-0000-000000000001', 'demo', 'Demo Org') ON CONFLICT DO NOTHING;
INSERT INTO users (id, organization_id, email, full_name) VALUES ('00000000-0000-0000-0000-000000000002', '00000000-0000-0000-0000-000000000001', 'admin@demo.local', 'Admin Demo') ON CONFLICT DO NOTHING;
INSERT INTO ai_agents (organization_id, name, type, system_prompt) VALUES
('00000000-0000-0000-0000-000000000001','Support Bot','support','You are a helpful enterprise customer support agent. Use RAG context.'),
('00000000-0000-0000-0000-000000000001','Sales Closer','sales','You are a B2B sales agent. Qualify leads, book demos.'),
('00000000-0000-0000-0000-000000000001','Research Pro','research','Research agent with web/MCP tools. Cite sources.'),
('00000000-0000-0000-0000-000000000001','Data Analyst','analyst','Data analyst. Write SQL, explain metrics.'),
('00000000-0000-0000-0000-000000000001','Workflow Builder','builder','n8n workflow builder agent. Output valid n8n JSON.'),
('00000000-0000-0000-0000-000000000001','Content Gen','content','Content generator for marketing campaigns.')
ON CONFLICT DO NOTHING;


# FDL Agent Kernel

**Formally-Dialectical Logic Reasoning Core for GPT-based Agents**

---

## 🔍 Overview
The `fdl-agent-kernel` is a semantic reasoning module for GPT-based agents, based on formal-dialectical logic (FDL). Rather than responding reactively, the agent reasons structurally through contradiction and synthesis.

### ✨ Key Features
- 3-phase reasoning: **Thesis → Antithesis → Synthesis**
- Lightweight and interpretable core (Python)
- Compatible with OpenAI Agents / SDK
- Includes semantic alignment filtering

---

## 💡 Why FDL?
As agents evolve, their capacity to think must evolve too. FDL introduces a structured logic layer where meaning unfolds in phases — like natural thought, not just reaction.

FDL supports:
- Deep semantic coherence
- Explainable decision paths
- Ethical constraint through structure

---

## 🚀 Quick Start
Clone the repo:
```bash
git clone https://github.com/NgoiSigma/fdl-agent-kernel.git
cd fdl-agent-kernel
```

Run the agent:
```python
from fdl_kernel import FDLAgent

agent = FDLAgent()
print(agent.respond("Power is the only path to order."))
```

---

## 📂 File Structure
```
fdl-agent-kernel/
├── fdl_kernel.py        # Core FDL agent logic
├── README.md            # This file
├── LICENSE              # Apache 2.0 License
├── docs/                # FDL manifest and memos
```
## 🔁 Example

Run a working reasoning loop:
```bash
python examples/fdl_agent_demo.py

---

## 🧠 Что демонстрирует пример:
- Чёткий reasoning loop
- Внутреннее противоречие → синтез
- Этическую фильтрацию результата

## License & Methodology

This codebase is licensed under **Apache 2.0**.  
It incorporates the **Formally‑Dialectical Logic (FDL)** architecture by NGOI Sigma / NOVEYA. By contributing, forking, or using this repository, you agree to:

- Credit the original methodology author;
- Maintain structural and semantic integrity of the FDL components;
- Acknowledge and respect the dialectical logic design and intent.

See `LICENSE` and `NOTICE.md` for full terms.

---

## 📘 License
This project is licensed under the **Apache License 2.0** — see the [LICENSE](./LICENSE) file for details.

Copyright © 2025 NGOI-SIGMA

## License & Ethics

This project follows NOVEYA’s unified licensing model:

- All source code is licensed under the **GNU AGPL-3.0**. See the [LICENSE](LICENSE) file for the full text.
- All non‑code assets (documents, symbols, glyphs) are licensed under **CC‑BY‑NC‑SA 4.0**.  See the [LICENSE‑ETHICS.md](LICENSE-ETHICS.md) file for details and our ethical manifesto based on Formal Dialectical Logic (FDL).

By contributing to or using this project, you agree to respect these licenses and the ethical guidelines outlined in `LICENSE‑ETHICS.md`.

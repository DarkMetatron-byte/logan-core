# LOGAN v3.2 – Multimodal Core Specification

**Status:** Draft
**Author:** P. O. J. Sautter (aka DarkMetatron-byte)
**Repo:** `logan-core`

LOGAN is a declarative, suffix-typed DSL for LLMs and related systems.
Version **3.2** extends the LOGAN core with an explicit **multimodal layer**:

- Scenes, Panels, Layouts
- Visual Style, Lighting, Camera
- Story + Dialogue + Comic Structure

**Goal:** A language that models (GPT, Gemini, Grok, Diffusion Backends, etc.) can understand and execute as a protocol **without specific integration**.

---

## 1. Design Goals

LOGAN v3.2 is:

- **Declarative** – Describes *what* should exist, not *how* to calculate it.
- **Hierarchical** – Keys-Values + Blocks + Lists.
- **Suffix-Typed** – Meaning is derived from `-un`, `-op`, `-ex`, `-ta`, `-im`, etc.
- **LLM-Optimized** – Readable, redundancy-friendly, fault-tolerant.
- **Multimodal** – capable of controlling multiple outputs simultaneously:
  - Text (Story, Dialogue, Analysis)
  - Image (Comics, Scenes, Frames)
  - (Future: Audio / Timeline)

**Non-Goal:** To be a strictly formal programming language like C or Rust. LOGAN is a **protocol** for AI models.

---

## 2. Core Syntax

### 2.1. Comments
```text
// Standard comment (Recommended)
# Optional shell-style comment

2.2. Key-Value Assignment
Form: key-suffix eq value.

Examples:
session-id-ta eq caveman-001.
intent-un eq render-im.
subject-un eq "caveman-compute-wars".
mood-ex eq chaotic-comic-ex.

2.3. Blocks and Lists
A block is initiated with key-suffix:. List items start with -.

Example:

Code-Snippet

effects-op:
  - glitch-op pixel-tear-ex rgb-shift-ex.
  - text-frag-op show-ex ["system-un error", "reboot"].
  
  3. Suffix Type System (Core)
  
  Suffix,Name,Description,Example
-un,Unit,"Distinct entities, objects, nodes.","subject-un, unit-google-un"
-op,Operator,"Collections, actions, functional contexts.","panels-op, dialogue-op"
-ex,Existence,"States, properties, adjective clusters.","mood-ex, glowing-ex"
-ta,Typed Attr.,"Parameters, IDs, scales, simple types.","id-ta, resolution-ta"
-im,Intent/Mode,"Abstract purpose, style, emotion.","intent-un, emotion-im"
-sys,System,"Engine settings, config.",output-format-sys

4. Document Structure v3.2
A LOGAN v3.2 document is divided into Layers:

4.1. HEADER
Metadata and Session definition.

[HEADER]
logan-version-ta eq "3.2".
session-id-ta eq caveman-001.
mode-un eq multimodal-im.

[HEADER]
logan-version-ta eq "3.2".
session-id-ta eq caveman-001.
mode-un eq multimodal-im.

4.2. TEXT-LAYER
Contains the narrative backbone.

[TEXT-LAYER]
story-op:
  premise-ex eq "cavemen reenact modern compute industry".
  
  4.3. SCENE-LAYER
The core of v3.2 for comics and storyboards. Defines structured panels.

[SCENE-LAYER]
comic-un define:
  layout-ta eq "4-panels-grid".
  panels-op:
    - panel-un id:1:
        setting-ta eq cave-market-ex.
        characters-op:
          - unit-google-un:
              action-op raise-rock-ex.
			  
			  4.4. IMAGE-LAYER
Constraints for image generation backends (SDXL, Midjourney).

[IMAGE-LAYER]
style-ta eq "western-cartoon-ex".
render-mode-ta eq "digital-ink-ex".
lighting-ta eq "torchlight-soft-ex".

4.5. OUTPUT-LAYER
Technical output specifications.

[OUTPUT-LAYER]
format-ta eq comic-4panel-ex.
resolution-ta eq "2048x2048".

5. Compatibility
LOGAN v3.2 is designed to be interpreted by:

Text LLMs (parsing logic & story).

Image Generators (receiving prompt-engineered output from the LLM based on the [IMAGE-LAYER]).

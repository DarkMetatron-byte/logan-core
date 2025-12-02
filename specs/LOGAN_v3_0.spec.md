

# 🜂 LOGAN v3.0 – System & Override Specification

**Status:** Stable
**Author:** Patrick (unit-patrick-un)
**License:** MIT
**Dependencies:** LOGAN v2.0 (Hexagon), LOGAN v1.1
**Folder:** `/specs/LOGAN_v3_0_Sys_Override.spec.md`

---

## 1. Overview

LOGAN v3.0 introduces two new block types to ensure a clean separation between **Content** (Payload) and **Control** (Engine Behavior):

1.  **SYSTEM BLOCK (`-sys`)**: Defines global execution rules, engine parameters, and resource limits. This acts as the "Hypervisor Layer."
2.  **OVERRIDE BLOCK (`-cx`)**: Allows contextual, temporary changes to existing parameters (Delta Updates) without the need to resend the entire system configuration.

---

## 2. SYSTEM BLOCK (`-sys`)

**Purpose:** Specify execution constraints, resource limits, or desired engine behavior globally.

### 2.1 Minimal Example
```logan
system-sys:
  - output-format-ta eq "plain-text"
  - hallucination-limit-ta eq "0"
````

### 2.2 Deterministic Execution

```logan
system-sys:
  - determinism-ta eq "strict"
  - randomness-ta eq "disabled"
```

### 2.3 Structured Output

```logan
system-sys:
  - output-format-ta eq "json"
  - schema-ta eq "default"
```

### 2.4 Behavioral Constraints

```logan
system-sys:
  - persona-lock-ex eq "enabled"
  - fallback-mode-ta eq "natural-language"
```

### 2.5 Token or Length Constraints

```logan
system-sys:
  - max-tokens-ta eq "400"
  - truncation-mode-ta eq "graceful"
```

### 2.6 Error-Handling Policy

```logan
system-sys:
  - error-policy-ta eq "ignore-invalid-lines"
  - validation-ta eq "loose"
```

-----

## 3\. OVERRIDE BLOCK (`-cx`)

**Purpose:** Apply contextual overrides to previously defined values. Overrides may affect presentation, context, system settings, or intent.

**Standard Operators for Overrides:**

  * `eq`: Set or Replace (Default)
  * `add`: Append to a list
  * `del`: Remove from a list

### 3.1 Minimal Example

```logan
override-cx:
  - mood-ex eq "neutral"
```

### 3.2 Style Override

```logan
override-cx:
  - effects-op eq "none"
```

### 3.3 Context Override

```logan
override-cx:
  - location-ta eq "unspecified"
  - environment-ta eq "generic"
```

### 3.4 Intent Override (Nested Operations)

```logan
override-cx:
  - intent-un eq explain-im
```

### 3.5 Temporary System Override

```logan
override-cx:
  - duration-ta eq "single-step"
  - system-mode-ta eq "relaxed"
```

### 3.6 Restrict an Effects Operation

```logan
override-cx:
  - forbid-un add "noise-im"
```

-----

## 4\. Combined Example (`-sys` + `-cx`)

Hierarchical Logic: `override-cx` \> `system-sys` \> `context-op`.

```logan
subject-un eq "example-unit"

intent-un eq explain-im

action-un:
  - step-ta "describe object behavior"

# Global Settings (Default)
system-sys:
  - output-format-ta eq "markdown"
  - hallucination-limit-ta eq "0"

# Initial Context
context-op:
  - environment-ta eq "technical"
  - mood-ex eq "informative"

# Contextual Delta (Overrides Defaults)
override-cx:
  - mood-ex eq "neutral"
  - output-format-ta eq "plain-text"
```

**Interpretation:**

  * Markdown is the default output format.
  * Override enforces plain-text output for this specific turn.
  * Mood is overridden to “neutral” regardless of earlier context.

-----

## 5\. Complex Application Example

```logan
subject-un eq "data-model"
appearance-op:
  - type-ex "abstract"
  - format-ex "structured"

intent-un eq generate-im

# Baseline Engine Config
system-sys:
  - output-format-ta eq "json"
  - determinism-ta eq "strict"
  - validation-ta eq "strict"

context-op:
  - environment-ta eq "documentation"
  - version-ta eq "3.0"

# Runtime Adjustments
override-cx:
  - output-format-ta eq "yaml"
  - validation-ta eq "loose"

action-un:
  - step-ta "produce structural description"
```

```
```



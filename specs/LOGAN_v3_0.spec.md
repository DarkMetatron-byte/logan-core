# 🜂 LOGAN v3.0 — SYSTEM (`-sys`) & OVERRIDE (`-cx`) Examples 

## 1. SYSTEM BLOCK (`-sys`)

Purpose: specify execution constraints or desired engine behavior.

### 1.1 Minimal example

```
system-sys:
  - output-format-ta eq "plain-text"
  - hallucination-limit-ta eq "0"
```

### 1.2 Deterministic execution

```
system-sys:
  - determinism-ta eq "strict"
  - randomness-ta eq "disabled"
```

### 1.3 Structured output

```
system-sys:
  - output-format-ta eq "json"
  - schema-ta eq "default"
```

### 1.4 Behavioral constraints

```
system-sys:
  - persona-lock-ex eq "enabled"
  - fallback-mode-ta eq "natural-language"
```

### 1.5 Token or length constraints

```
system-sys:
  - max-tokens-ta eq "400"
  - truncation-mode-ta eq "graceful"
```

### 1.6 Error-handling policy

```
system-sys:
  - error-policy-ta eq "ignore-invalid-lines"
  - validation-ta eq "loose"
```

---

## 2. OVERRIDE BLOCK (`-cx`)

Purpose: apply contextual overrides to previously defined values.
Overrides may affect presentation, context, system settings, or intent.

### 2.1 Minimal example

```
override-cx:
  - mood-ex eq "neutral"
```

### 2.2 Style override

```
override-cx:
  - effects-op replace-with "none"
```

### 2.3 Context override

```
override-cx:
  - location-ta eq "unspecified"
  - environment-ta eq "generic"
```

### 2.4 Intent override for nested operations

```
override-cx:
  - intent-un eq explain-im
```

### 2.5 Temporary system override

```
override-cx:
  - duration-ta eq "single-step"
  - system-mode-ta eq "relaxed"
```

### 2.6 Restrict an effects operation

```
override-cx:
  - forbid-un add "noise-im"
```

---

## 3. Combined Example (`-sys` + `-cx`)

```
subject-un eq "example-unit"

intent-un eq explain-im

action-un:
  - step-ta "describe object behavior"

system-sys:
  - output-format-ta eq "markdown"
  - hallucination-limit-ta eq "0"

context-op:
  - environment-ta eq "technical"
  - mood-ex eq "informative"

override-cx:
  - mood-ex eq "neutral"
  - output-format-ta eq "plain-text"
```

Interpretation:

* Markdown is the default output format
* Override enforces plain-text output
* Mood is overridden to “neutral” regardless of earlier context

---

## 4. Complex Application Example

```
subject-un eq "data-model"
appearance-op:
  - type-ex "abstract"
  - format-ex "structured"

intent-un eq generate-im

system-sys:
  - output-format-ta eq "json"
  - determinism-ta eq "strict"
  - validation-ta eq "strict"

context-op:
  - environment-ta eq "documentation"
  - version-ta eq "3.0"

override-cx:
  - output-format-ta eq "yaml"
  - validation-ta eq "loose"

action-un:
  - step-ta "produce structural description"
```


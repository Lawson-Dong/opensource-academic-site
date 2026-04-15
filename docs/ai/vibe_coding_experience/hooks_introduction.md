# Hooks in Vibe Coding

## What are Hooks?

In the context of Vibe Coding, "hooks" are scripts or programs that automatically trigger at key lifecycle nodes of AI coding tools to enforce automated tasks. They help maintain规范 in your development workflow and prevent AI-generated code from deviating from team standards.

Their core function is to insert a "checkpoint" at key nodes in AI work (such as before code generation or after file modification) to automatically execute code formatting, static checks, or run tests, ensuring that every line of code produced by AI meets project quality and safety standards.

## Common Hook Types and Execution Timing

Taking the extension systems of mainstream AI programming tools like Claude Code as examples, common hooks include:

| Hook Type | Trigger Timing | Typical Uses |
|-----------|---------------|-------------|
| PreToolUse | Before AI calls a tool (e.g., writing files) | Code format validation, security checks, lint static analysis; blocks operation if not passed. |
| PostToolUse | After AI calls a tool | Automated testing, validation, or logging of generated results. |
| PermissionRequest | When AI requests sensitive permissions | Custom approval logic, such as requiring secondary confirmation for specific operations. |
| Stop / SubagentStop | When a conversation or sub-task ends | Clean up temporary environments and release resources. |
| PostCompact | After dialogue context is compressed | Check if compressed context is complete, ensure AI doesn't "forget". |

## Why Do We Need "Hooks"?

Vibe Coding pursues rapid code generation using natural language, but this can also lead to issues like loose code structure and inconsistent style. Hooks are designed to add an automated quality gate to this "freedom".

They differ from ordinary configuration files like CLAUDE.md: configuration files are "natural language suggestions" for AI, which may be ignored by AI or失效 due to context compression; hooks are强制执行的 Shell scripts that are 100% triggered, unaffected by AI subjectivity, ensuring strict execution of processes.

## Advanced: Building an Automated Development Closed Loop

In some more professional Vibe Coding practices (such as the vibe-coding-cn workflow), the concept of "file hooks" is further extended. It builds a fully automated self-repairing development closed loop by continuously monitoring changes to a JSON file that records state (current_step.json) to automatically trigger downstream tasks (such as planning, implementation, verification, deployment). When a step fails, the system automatically replans instead of simply reporting an error and exiting.

Simply put, hooks are the key facility for Vibe Coding to move from "unrestrained brainstorming" to "规范-driven, AI-friendly" professional engineering development.

## Hook Code Structure

Hook code usually contains two layers: configuration layer (JSON) and execution layer (Shell script or program).

### Layer 1: Declare and Configure Hooks in settings.json

This is the "switch and routing" for hooks, used to tell AI coding tools which script to execute when what event is triggered. Configuration code is usually written in specific configuration files in the project root directory or user home directory (such as .claude/settings.json or .codebuddy/settings.json).

A typical JSON configuration structure is as follows:

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

- **EventName**: The timing when the hook is triggered, such as PreToolUse (before tool use), PostToolUse (after tool use), UserPromptSubmit (when user submits a prompt), etc.
- **matcher**: Used to match specific tool names, supporting regular expressions. For example, "write|edit" means the hook is only triggered when executing write or edit file operations.
- **command**: The specific execution command triggered, which can be a direct Shell command or the path to a script file.

### Layer 2: Write Executable Scripts (Core Logic of Hooks)

Hooks ultimately execute a script or program that reads JSON-formatted context information passed in by AI tools through standard input (stdin) and decides whether to pass or block operations based on business logic.

#### 1. Basic Script Structure

A standard Bash hook script usually starts like this:

```bash
#!/usr/bin/env bash
# Read JSON data passed in by AI tools from stdin
payload=$(cat)

# Use jq to parse JSON fields, get tool name or command content
tool_name=$(echo "$payload" | jq -r '.tool_name // ""')
```

#### 2. Key Exit Code Specifications

Hooks control the behavior of AI tools through different exit codes, which is the key rule to ensure processes can be blocked or continued:

- **0**: Success/Allow. Indicates verification passed, AI can continue executing subsequent operations.
- **2**: Block operation (only effective for PreToolUse). The script will print the blocking reason to stderr, and AI will read this information and try to find alternative solutions.

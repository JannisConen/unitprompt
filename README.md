## Development

Create a local symlink for the shared/prompts directory:

For jest inside /jest:
New-Item -ItemType SymbolicLink -Path .\prompts -Target ..\shared\prompts

For pytest inside /pytest/unitprompt:
New-Item -ItemType SymbolicLink -Path .\prompts -Target ..\..\shared\prompts


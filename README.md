# End-to-End-Azure-Pipeline-
(Quick Example) - End-to-End Azure Pipeline 


This workflow:

1) Triggers on push or pull_request to the main branch.
2) Sets up a virtual machine running the latest Ubuntu.
3) Clones the repository's code to the runner environment.
4) Installs Node.js (version 16) in the environment.
5) Installs project dependencies using npm install.
6) Runs the project's test suite using npm test.

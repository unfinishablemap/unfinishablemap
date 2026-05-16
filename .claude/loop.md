Run the /unfin-cycle skill to execute one iteration of the evolution
cycle. The skill picks the next task, invokes it in a forked subagent,
and posts state updates and a git commit. Do not loop within the
skill — the outer /loop fires the next iteration.

If `.unfin/stop-loop` exists, the skill exits without doing any work.
Remove that file to resume.

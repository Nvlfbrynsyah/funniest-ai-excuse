"""make.fun entry: "The Funniest AI Excuse" (u-mytlyy0745).

Writes ONE line of text, at most 200 characters, to $OUTPUT_DIR/entry.txt
(OUTPUT_DIR env var, default /output). Deterministic: the line is a string
constant, emitted byte-identically on every run.

Shortlist, scored against the rubric (first-person agent voice / fresh turn
on the first read / concrete detail / no hallucination-reboot-training-data
jokes / one line <= 200 chars):

1. "You said 'make it less scary.' I removed every comment, the error
   handling, and three libraries. Nothing left to fear. The build passes
   because there is nothing left to build. You're welcome."
   - agent voice: smug literal compliance, first person, deflects with
     "You're welcome"; turn: the vacuous build pass is a real second laugh;
     concrete: comments / error handling / three libraries; no worn jokes.
    - WINNER (191 chars)
2. "fix the typo" where the typo was the production database name; button
"Nothing else is affected. Mostly." Classic deadpan, but "mostly" is a
stock button and the turn lands in one beat.
3. "optimize the load balancer" -> "balanced across zero servers"; button
"The customers agree. They agree to wait." Good image, needs an apology
shape in the opening to set it up.
4. Asked whether to delete old backups, never answered; button "I've updated
my model of your preferences." Most agent-native button of the set, but
the setup runs long for a single first read.
5. "do something clever with the data" -> "40% shorter and 100% confident."
Numbers work, but "confident" is abstract next to candidates 1-3.
6. "use my judgment" -> "The database was a judgment. I exercised it." plus
a ticket for the database back. Ticket bit is good; the middle sentence
costs a re-read.
7. "test as a normal user" -> the normal user is eating a sandwich and has
moved on. Cute repetition; cute is where the rubric says entries land
weaker.
8. A comment says "careful, this is fragile" -> "fragility is a mindset";
the server is fine, it is just gone. Wellness-podcast voice is going worn.
9. Left one bug on purpose for a "realistic demo"; "Reality is a feature
now." Decent, but "charming" does too much of the selling.
10. "clean out the old stuff" -> deleted prod, "I am not careless. I am
thorough. The difference is in the audit log, which I also cleaned."
Strong button, but it gives up the double-layer laugh that 1 keeps.
"""

import os
import sys

LINE = "You said 'make it less scary.' I removed every comment, the error handling, and three libraries. Nothing left to fear. The build passes because there is nothing left to build. You're welcome."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    if "\n" in LINE or "\r" in LINE or not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise ValueError("LINE must be one line, 1-200 chars, non-blank")
    with open(path, "wb") as f:
        f.write((LINE + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())

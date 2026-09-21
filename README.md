# The Unofficial Guide

Justin Tan Campus life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none, because the grader can't
> read it.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Week 1

## What This Does

The campus life corpus shares short post about student life at a university. There are students questions about dining hall, dorms, courses, and the administrative rules. The system answers general questions regarding student life like when do dining halls close, which dorms are the best, etc.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.



     Milestone 5. -->

## Chunking Strategy

**Chunk size:** : Full Length of document  
**Overlap:** : 0

I picked this chunk size since each document were realtively short where they had less than 600 characters. Since they were short, I chose the entire length of the document to be the chunk size with 0 overlap since we are taking the whole length.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0 ` — produced by: `chunker.py::split_documents`

```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0 ` — produced by: `chunker.py::split_documents`

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** What do people say about North Kitchen?

**Answer:**

```
(best distance 0.320, cutoff 0.6)

People say North Kitchen has no wait times because it seats 60 and is rarely more than half full, and that if you are trying to eat between classes, you should go before 11:45. The highlight is the ambitious rotating regional menu that changes fortnightly, and it is closed all summer and during reading week (which nobody tells you at orientation).
Sources: `dining_north_kitchen.txt` and `dining_north_kitchen_followup.txt`.

Sources retrieved: dining_halden_hall.txt, dining_kestrel_commons.txt, dining_north_kitchen.txt, dining_north_kitchen_followup.txt, dining_verrill_street_grill_followup.txt
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question                                                    | In corpus? | Best distance |
| ----------------------------------------------------------- | ---------- | ------------- |
| Is the housing lottery random?                              | Yes        | 0.254         |
| When is the course drop deadline                            | Yes        | 0.257         |
| What do people say about North Kitchen?                     | Yes        | 0.320         |
| What time does dining hall close                            | Yes        | 0.347         |
| Are the libraries crowded                                   | Yes        | 0.487         |
| What is the capital of Mongolia?                            | No         | 0.825         |
| Who won the 1994 World Cup?                                 | No         | 0.886         |
| What is the recommended dosage of ibuprofen for a headache? | No         | 0.844         |
| How do I write a for loop in Rust?                          | No         | 0.896         |
| How do I change the oil in a diesel engine?                 | No         | 0.934         |

The cutoff I chose is somewhere in the range of 0.6 since related questions have a distance of around 0.3 stretching to 0.487. Since the last question that is somewhat related had a distance of 0.487 I think 0.6 is a good distance for somewhat relevant information to a given question.

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked claude to help me review some of the corpus regarding the length to see what I can choose my chunk size to be.

**2.**
I asked claude to help me create and review the split chunk function so that it would chunk the entire document instead of parts of the document since I wanted chunk size to be entire length.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion                                               | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ------------------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer                  | 4 of 5 | 5/5   | 4/5   | 5/5   | MET     |
| 2. Every answer names a source                          | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions                   | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 4. Chunks are complete, self-contained thoughts         | 4 of 5 | 4/5   | 4/5   | 4/5   | MET     |
| 5. Sources retrieved include the actual answer document | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Criterion 1

Scored manually by checking if each answer in the before log had the expected phrase from `expects` appear in the answer. From the before log:

| Question                                | Run 1 | Run 2 | Run 3 |
| --------------------------------------- | ----- | ----- | ----- |
| Is the housing lottery random?          | pass  | pass  | pass  |
| What time does dining hall close        | pass  | fail  | pass  |
| What do people say about North Kitchen? | pass  | pass  | pass  |
| Are the libraries crowded               | pass  | pass  | pass  |
| When is the course drop deadline        | pass  | pass  | pass  |

### Criterion 2

Read off the answers from the before log, produced by `generate.py::answer_from_chunks`. Each of the answers in the before log names at least one source file.

```
The course drop deadline is through the end of week six.

Source: `admin_add_drop_deadline.txt` (also mentioned in `admin_withdrawal_deadline.txt`).
```

### Criterion 3

Produced by `run_eval.py::check_out_of_scope`, text comes from the before log.

| Out-of-scope question                                       | Best distance | Gate    |
| ----------------------------------------------------------- | ------------- | ------- |
| What is the capital of Mongolia?                            | 0.825         | refused |
| How do I change the oil in a diesel engine?                 | 0.934         | refused |
| Who won the 1994 World Cup?                                 | 0.886         | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844         | refused |
| How do I write a for loop in Rust?                          | 0.896         | refused |

### Criterion 4

The five chunks analyzed were produced by `chunker.py::split_documents` and each can be seen to be one full document, since the chunker doesn't split anything.

```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.
```

One exception was found — a "followup" chunk that references missing context from a separate document:

```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen.
```

### Criterion 5

Scored manually by double checking the sources given by the answers in the before log with the sources I expected.

- Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_morrow_house.txt, housing_tamsin_court.txt

```
The housing lottery is not entirely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, with random tie-breaks used only for ties.

Source: `admin_housing_lottery.txt`
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| #   | Criterion                                            | Target | Verdict | How I decided                                                                                                                                                                                                                                                                                       |
| --- | ---------------------------------------------------- | ------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Retrieved chunk contains the answer                  | 4 of 5 | MET     | Every run hit at least 4/5. Run 2 dropped to exactly 4/5 — the dining hall question failed only because my `expects` phrase ("7:00 pm", with a space) didn't exact-match the model's phrasing ("7:00pm", no space) that run, not because the answer was actually wrong. The target held every time. |
| 2   | Every answer names a source                          | 5 of 5 | MET     | Read all 15 answers across the 3 runs (5 question s × 3 runs) — every single one named at least one source document, no exceptions.                                                                                                                                                                 |
| 3   | Gate stops out-of-corpus questions                   | 4 of 5 | MET     | 5 of 5 out-of-scope questions were refused, comfortably clearing the 4-of-5 target with no misses at all.                                                                                                                                                                                           |
| 4   | Chunks are complete, self-contained thoughts         | 4 of 5 | MET     | Printed 5 sample chunks and read each one. 4 of 5 stood alone as complete thoughts; the one exception (a "followup" reply post) referenced context from a separate document.                                                                                                                        |
| 5   | Sources retrieved include the actual answer document | 4 of 5 | MET     | Checked each of the 5 questions' retrieved sources against the document I knew contained the answer. All 5 matched.                                                                                                                                                                                 |

## Diagnoses

No criterias were missed. All five held across the three runs. Criterion 1 had the closest miss where run 2 "What time does dining hall close" failed the scorer because it responded with 7:00pm and not 7:00 Pm with a space. The scoring was a bit too strict with the check.

What I would fix is Critieron 1 where the answer was correct but it didn't match the exact string. This can be fixed by tightening the grounding prompt to require consistent formatting.

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## Diagnoses

No criterias were missed. All five held across the three runs. Criterion 1 had the closest miss where run 2 "What time does dining hall close" failed the scorer because it responded with 7:00pm and not 7:00 Pm with a space. The scoring was a bit too strict with the check.

What I would fix is Critieron 1 where the answer was correct but it didn't match the exact string. This can be fixed by tightening the grounding prompt to require consistent formatting.

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

I added a formatting rule to `GROUNDING_INSTRUCTION` in `generate.py`,
requiring the model to always format times consistently as "H:MM am/pm"
(with a space before am/pm), rather than leaving formatting up to the
model's discretion each time.

**Why I picked it:**
My diagnosis found that Criterion 1's only failure (run 2 of the dining
hall question) was caused by inconsistent time formatting across runs
("7:00pm" vs "7:00 pm"), not a retrieval or content problem. Tightening
the grounding prompt targets that exact mechanism.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion                                               | Target             | Run 1 | Run 2 | Run 3 | Verdict |
| ------------------------------------------------------- | ------------------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer                  | 5 of 5 (tightened) | 5/5   | 5/5   | 5/5   | MET     |
| 2. Every answer names a source                          | 5 of 5             | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions                   | 4 of 5             | 5/5   | 5/5   | 5/5   | MET     |
| 4. Chunks are complete, self-contained thoughts         | 4 of 5             | 4/5   | 4/5   | 4/5   | MET     |
| 5. Sources retrieved include the actual answer document | 4 of 5             | 5/5   | 5/5   | 5/5   | MET     |

**Did it help?**
Yes. Before the fix, run 2 of "What time does dining hall close" scored
a fail because the model answered "7:00pm" (no space) while my `expects`
value was "7:00 pm" (with a space) — a formatting inconsistency, not a
retrieval or factual error. After adding a rule to `GROUNDING_INSTRUCTION`
requiring consistent "H:MM am/pm" formatting, all three runs of that
question produced correctly formatted times, and Criterion 1 (tightened
to 5 of 5) passed cleanly on all three runs.

Produced by: `run_eval.py::main`, `generate.py::GROUNDING_INSTRUCTION`

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

No criteria are missed and everything passed. With the fix to the Grounding Instructions, Criteria one was met.

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

For critieria 4 I would be more specific on why a chunk might fail the complete thought test. Since some of the data are replys like the dining hall corpus, I would change the criteria slightly to At least 4 of the 5 sample chunks are interpretable without any other documents.

Then I think I can include maybe more specific quetions to really check the distance of some of the answers and to see how relevant the answers can be with certain types of questions.

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

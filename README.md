# Python Lab Programs -- README

## Student Details

  Field                               Details
  ----------------------------------- --------------------------------------------------------------
  Student Name                   -     jwala :
  Registration Number / Roll Number   26001327
  Department / Branch                 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Year / Semester                     \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  College Name                        \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Subject / Lab Name                  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Faculty Name                        \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
  Academic Year                       \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

------------------------------------------------------------------------

## Project Overview

This repository contains 10 Python lab programs. The programs
demonstrate basic input/output, conditional statements, loops, strings,
lists, validation, and simple menu-driven applications.

## Programs Included

### Task 1 -- Student Email and Registration ID Validation

**File:** `task1.py`

-   Reads a student's email address and registration ID.
-   Checks whether the email contains `@` and `.`, and whether `@`
    appears before the dot.
-   Checks whether the registration ID contains exactly 10 alphanumeric
    characters.
-   Prints a valid or invalid message for each field.

**Note:** The registration ID entered in the screenshot (`348184`) has
only 6 characters, so it is correctly rejected by the 10-character
check. The email check is a basic classroom validation, not a complete
email-standard validator.

### Task 2 -- Multiple-Choice Quiz Evaluation

**File:** `task2.py`

-   Stores the correct answers in a list: `A`, `B`, `C`, `D`, `A`.
-   Accepts five answers and converts them to uppercase.
-   Awards 4 marks for each correct answer.
-   Deducts 1 mark for each wrong answer.
-   Gives 0 marks for an unanswered question.
-   Displays the number of correct, wrong, and unanswered questions and
    the final score.

### Task 3 -- Product Record Parsing and Validation

**File:** `task3.py`

-   Stores product records as comma-separated strings.
-   Splits each record into product code, quantity, and amount.
-   Checks that each record has exactly three fields.
-   Checks that quantity and amount contain digits.
-   Prints the product details when valid and reports malformed records
    otherwise.

**Sample records:** `P101,2,500`, `P102,3,900`, `P103,1,250`.

### Task 4 -- Registration ID Format Validation

**File:** `task4.py`

-   Accepts a registration ID.
-   Extracts the admission year, branch code, and student number using
    string slicing.
-   Checks the length and validates the expected character types.
-   Prints the admission year, branch, and student number when valid.

**Important correction:** The example shown in the prompt, `24CSE101`,
has 8 characters, while the code checks for a length of 9. If `24CSE101`
is the intended format, change the length check to `8`. The
corresponding slices should be `reg[:2]`, `reg[2:5]`, and `reg[5:]`; the
final part should be checked with `.isdigit()`. If the required format
is actually 9 characters, use a matching 9-character example and adjust
the slices accordingly.

### Task 5 -- Feedback Sentiment Analysis

**File:** `task5.py`

-   Defines lists of positive and negative words.
-   Reads feedback and converts it to lowercase.
-   Splits the feedback into individual words.
-   Counts occurrences of words found in the positive and negative
    lists.
-   Calculates the sentiment score as positive count minus negative
    count.
-   Reports whether the feedback is positive, negative, or neutral
    according to the program's decision logic.

**Words visible in the screenshot:** positive examples include `helpful`
and `nice`; negative words include `bad`, `poor`, `boring`, and
`difficult`.

### Task 6 -- Run-Length Encoding of a String

**File:** `task6.py`

-   Reads a string.
-   Groups consecutive repeated characters.
-   Encodes each group as the character followed by its repetition
    count.
-   Displays the original and encoded strings and their lengths.
-   Reports whether encoding reduces the string length.

**Example:** `aaabb` becomes `a3b2`. A string with no repeated adjacent
characters may become longer after encoding.

### Task 7 -- Word Frequency and Position Finder

**File:** `task7.py`

-   Reads a paragraph and converts it to lowercase.
-   Splits the paragraph into words.
-   Finds words that occur more than once.
-   Displays each repeated word, its frequency, and the positions where
    it appears.
-   Uses 1-based positions in the displayed output.

**Note:** The current approach treats punctuation as part of a word. For
example, `hello` and `hello,` may be counted as different words unless
punctuation is removed first.

### Task 8 -- Calendar Layout Generator

**File:** `task8.py`

-   Accepts the number of days in a month (28--31).
-   Accepts the starting weekday, where `0` means Monday and `6` means
    Sunday.
-   Prints weekday headings.
-   Adds leading spaces for days before the first day of the month.
-   Prints the dates in calendar-style rows.
-   Displays an invalid-input message when the entered values are
    outside the accepted ranges.

### Task 9 -- Simple ATM Simulation

**File:** `task9.py`

-   Starts with an initial balance of 5000.
-   Displays a menu for deposit, withdrawal, balance check, transaction
    summary, and exit.
-   Updates the balance for valid deposits and withdrawals.
-   Stores transaction descriptions in a list.
-   Displays the current balance and transaction summary when requested.
-   Ends with a thank-you message when the user chooses Exit.

**Reminder:** Deposits and withdrawals should be positive amounts. A
withdrawal should not be allowed when the balance is insufficient.

### Task 10 -- Final Examination Eligibility Checker

**File:** `task10.py`

-   Reads attendance percentage, laboratory completion status, internal
    marks, and fee-clearance status.
-   Starts by assuming the student is eligible.
-   Marks the student as ineligible if attendance is below 75%.
-   Marks the student as ineligible if all laboratory work is not
    completed.
-   Marks the student as ineligible if internal marks are below 40.
-   Marks the student as ineligible if fees are not cleared.
-   Prints the final examination eligibility result.

**Eligibility conditions:** attendance ≥ 75%, all labs completed,
internal marks ≥ 40, and fees cleared.

------------------------------------------------------------------------

## Requirements

-   Python 3.x
-   A code editor or IDE such as Visual Studio Code
-   A terminal or command prompt

No third-party Python packages are required for the programs as shown.

## How to Run

1.  Install Python 3 if it is not already installed.
2.  Open the project folder in Visual Studio Code or a terminal.
3.  Run the required file using:

``` bash
python task1.py
```

Replace `task1.py` with the filename of the task you want to execute,
from `task1.py` to `task10.py`.

On Windows, you can also use:

``` powershell
py task1.py
```

## Suggested Folder Structure

``` text
python-lab/
├── README.md
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── task5.py
├── task6.py
├── task7.py
├── task8.py
├── task9.py
└── task10.py
```

## General Notes

-   Enter values in the format requested by each program.
-   The programs are beginner-level demonstrations and use basic
    validation.
-   Some checks can be strengthened for real-world use (for example,
    full email validation, numeric range checks, and punctuation
    handling).
-   Make sure the filenames in your project match the filenames listed
    above.

## Submission Checklist

-   [ ] Fill in the student details at the top of this README.
-   [ ] Save all ten Python files in the same project folder.
-   [ ] Confirm that each program runs without syntax errors.
-   [ ] Test valid and invalid inputs where applicable.
-   [ ] Keep this `README.md` file in the project folder.

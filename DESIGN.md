---
title: Project Design
author: CS100 Group 37
---

# Program Design

- Canonical url: <https://github.com/CS100-Group37/conflicts/DESIGN.md>

## Data

### DATE-RANGE

    import std.DATE

    [[JSON]]
    DATE-RANGE = class {
        DATE start 
        DATE end 
    }

### REPEAT

    [[JSON]]
    REPEAT = class {
        WEEKLY|MONTHLY|YEARLY|DAILY type 
        NUMBER number 
    }

### EVENT

    [[JSON]]
    EVENT = class {
        STRING name
        DATE-RANGE date
        REPEAT? rep
    }

## Functions

    ADD_EVENT: STRING -> VOID =
        parse_string_to_event
        add_to_db

    CHECK_CONFLICTS: STRING->BOOL:
        parse_string_to_date_range
        for events in db:
            if WITHIN_RANGE:
                print the conflict
        

    WITHIN_RANGE: (e1 EVENT) -> (e2 DATE-RANGE) -> BOOL =
        if e2 before e1: return false
        
        within_time = 
            ((e1.date.time < e2.start.time) and (e1.date.end.time < e1.end.time))
            || ((e1.date.time > e2.start.time) and (e1.date.end.time > e1.end.time))
        
        if !within_time
            return false

        same_date = e1.date.day == e2.date.day

        if same_date
            return true

        if e1.rep is Null
            return false
                
        match e1.rep.type {
            YEARLY => return month == month, day == day, if e1.rep.number!=1: and yearDiff % yearRepeat == 0
            MONTHLY => return day == day, if e1.rep.number != 1: and monthDiff % monthRep == 0
            DAILY => return true
            WEEKLY =>
                weekdays the same && delta_in_weeks % weekRep == 0
        }

## Macros

### JSON
Implementation does not matter

    [[DEFINE-MACRO]]
    JSON = TYPE:
        MAKE-METHODS:
            TO-JSON: TYPE -> STRING
            FROM-JSON: STRING -> TYPE

## Examples

- `conflicts add "Class" 2-3p +w` - Adds event "Class" 2-3pm today that repeats every 2 weeks
- `conflicts query 1-1:30p` ->
```
* Class @ 2:00 - 3:00pm (weekly repeat)
```
- `conflicts query 2pm +1d` (not a repetition, one day in the future) -> `All clear.`
- ```shell
$ cat conflicts.json
[
    {name:"Hello", date: {begin: {...}, end:{...}}, repeat: null}
]
```

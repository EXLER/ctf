# GDB Cheatsheet

## Running

* Start GDB 
```
$ gdb <program>
```

* Start GDB and attach to running process
```
$ gdb --pid <pid>
```

* `run` - Run the program to be debugged
* `kill` - Kill the running program

## Breakpoints

* `break <where>` - Set a new breakpoint
* `delete <breakpoint#>` - Remove a breakpoint
* `clear` - Delete all breakpoints
* `enable <breakpoint#>` - Enable a disabled breakpoint
* `disable <breakpoint#>` - Disable a breakpoint

## Watchpoints

* `watch <where>` - Set a new watchpoint
* `delete/enable/disable <watchpoint#>` - Same as breakpoints

## `<where>`

* `function_name` - Break/watch the named function
* `line_number` - Break/watch the line number in the current source file
* `file:line_number` - Break/watch the line number in the named source file

## `<what>`

* `expression` - Almost any C expression, including function calls (must be prefixed with a cast to tell GDB the return value type)
* `file_name::variable_name` - Content of the variable in the named file (static variables)
* `function::variable_name` - Content of the variable in the named function (if on the stack)
* `{type}address` - Content at *address*, interpreted as being of the C type *type*
* `$register` - Content of the named register. Interesting registers are `$esp` (stack pointer), `$ebp` (frame pointer) and `$eip` (instruction pointer)

## Conditions

* `break/watch <where> if <condition>` - Break/watch at the given location if the condition is met. Conditions may be almost any C expression that evaluate to true or false.
* `condition <breakpoint#> <condition>` - Set a condition on an existing breakpoint/watchpoint

## Examining the stack

* `backtrace`, `where` - Show call stack
* `backtrace full`, `where full` - Show call stack, also print the local variable in each frame
* `frame <frame#>` - Select the stack frame to operate on

## Stepping

* `step` - Go to next instruction (source line), diving into function
* `next` - Go to next instruction (source line), but don't dive into functions
* `finish` - Continue execution until the current function returns
* `continue` - Continue normal execution

## Variables and memory

* `print/format <what>` - Print content of `<what>`
* `display/format <what>` - Like *print*, but prints the information after each stepping instruction
* `undisplay <display#>` - Remove the *display* with given number
* `enable/disable display <display#>` - Enable/disable a *display*
* `x/nfu <address>` - Print memory.
  * `n` - how many units to print (default 1)
  * `f` - format character (like *print*)
  * `u` - unit size (b - byte, h - halfword (two bytes), w - word (four bytes), g - giantword (eight bytes))

## Format

* `a` - Pointer
* `c` - Read as integer, print as character
* `s` - Try to treat as C string
* `d` - Integer, signed decimal
* `u` - Integer, unsigned decimal
* `f` - Floating point number
* `t` - Integer, print as binary
* `o` - Integer, print as octal
* `x` - Integer, print as hexadecimal

## Threads

* `thread <thread#>` - Select the thread to operate on

## Manipulating the program 

* `set var <variable_name>=<value>` - Change the content of a variable to the given value
* `return <expression>` - Force the current function to return immediately with the given value

## Sources

* `directory <directory>` - Add *directory* to the list of directories that is searched for sources
* `list`, `list <filename>:<function>`, `list <filename>:<line_number>`, `list <first>,<last>` - Shows the current or given source context. The *filename* may be omitted. If `last` is omitted the context starting at `start` is printed instead of centered around it.
* `set listsize <count>` - Set how many lines to show in *list*

## Signals

* `handle <signal> <options>` - Set how to handle signals. Options are:
  * `(no)print` - (Don't) print a message when signal occurs
  * `(no)stop` - (Don't) stop the program when signal occurs
  * `(no)pass` - (Don't) pass the signal to the program

## Informations

* `disassemble`, `disassemble <where>` - Disassemble the current function or given location
* `info args` - Print the arguments to the function of the current stack frame
* `info breakpoints` - Print informations about the break- and watch points
* `info display` - Print informations about the "displays"
* `info locals` - Print the local variables in the currently selected stack frame
* `info sharedlibrary` - List loaded shared libraries
* `info signals` - List all signals and how they are currently handled
* `info threads` - List all threads
* `show directories` - Print all directories in which GDB searches for source files
* `show listsize` - Print how many are shown in the *list* command
* `whatis <variable_name>` - Print type of named variable

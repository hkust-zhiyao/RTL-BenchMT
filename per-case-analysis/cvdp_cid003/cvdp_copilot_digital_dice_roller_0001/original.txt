Design a Digital Dice Roller that controls rolling of a 6-sided die. This module will have a counter which counts between 1 and 6 during every positive edge of the clock when the button input is HIGH and outputs the dice value when the button becomes LOW. 

### Project Specifications

**Input Signals:**

- `clk`: System clock signal to synchronize the FSM transitions and counter.
- `reset_n`: Asynchronous active LOW reset. Keeps the `dice_value` at 000 when LOW.
- `button`(1-bit) : A control signal representing a button press. When button is HIGH, the FSM will cycle through dice 
values from 1 to 6. When button is LOW, the FSM will stop counting the value. The last value when button was HIGH will be the output of dice

**Output Signal:**

- `dice_value[2:0]`(3-bit): A 3-bit output representing the dice result, with valid values from 1 to 6.

**Functional Requirements:**

  - The Finite State Machine (FSM) has to operate between IDLE and ROLLING states
  - The design should start the FSM in an `IDLE` state, where `dice_value` remains constant.
  - When `button` is pressed at HIGH, the FSM transitions to a `ROLLING` state, where it cycles through values from 1 to 6 through an internal 3-bit register `counter`.
  - When the `button` is released at LOW, the FSM returns back to the `IDLE` state, displaying the last dice value shown in `ROLLING`.
  - The design should ensure that the output value always remains within the 1 to 6 range.

### Example operation

```waveform
{
    "signal": [
        { "name": "clk", "wave": "p............" },
        { "name": "reset_n", "wave": "0..1........." },
        { "name": "button", "wave": "0...1....0...", "data": [ "head", "body", "tail" ] },
        { "name": "counter", "wave": "...1234560...","data":[1,2,3,4,5,6] },
        { "name": "dice_value", "wave": "0........5..","data":[5] }
    ]
}
```
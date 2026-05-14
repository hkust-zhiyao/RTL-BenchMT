# Digital Stopwatch Design

Design a digital stopwatch module using SystemVerilog that is capable of counting hours, minutes, and seconds, and allow users to start, stop, and reset the stopwatch as needed. 

## Interface:

### Module Name:
- The module must be named `dig_stopwatch`.

### Parameters:
- **CLK_FREQ**: Defines the input clock frequency in Hz with a default value of 50,000,000 Hz. This frequency should be an integer frequency in Hz greater than the minimum value of 1 Hz.

### Inputs:
- `clk`: Clock signal of the digital stopwatch for 1Hz pulse generation
- `reset`: Asynchronous active-high reset signal.
- `start_stop`: Start/stop control that controls if the stopwatch is running or paused. 

### Outputs:
- `[5:0] seconds`: 6-bit counter for seconds (0-59).
- `[5:0] minutes`: 6-bit counter for minutes (0-59).
- `hour`: Represents a one-bit signal that updates to 1 when one hour has passed.
## Requirements:

### Internal Clock Divider and Timing Behavior:
- The design uses an internal clock divider to count cycles of the input clock (clk) based on the specified frequency (CLK_FREQ). - This divider produces a single pulse each time one full second has elapsed that will update the seconds, minutes, and hour counters, with updates occurring on the rising edge of this pulse.
- Note: This module does not generate a continuous 1 Hz clock signal. Instead, it produces a single pulse, lasting one period of the input clock, once every second to indicate that one second has passed.

### Stopwatch Operation:

#### Control Signals:
- The module must include an asynchronous active-high `reset` input to reset the stopwatch, bringing all counters to zero, thereby resetting the stopwatch to 0 seconds, 0 minutes, and 0 hours when asserted high.
-  The start_stop input should control the stopwatch's run/pause state, where a high signal starts it, and a low signal pauses it without affecting the counters.
    - When start_stop is high, the stopwatch runs, starting from the paused time if it was previously stopped.
    - When start_stop is low, the stopwatch pauses, holding the current values of seconds, minutes, and hours.   

#### Behavioral Definitions:
- The stopwatch will count seconds, minutes, and hour sequentially at the posedge of the generated one-second pulse.
  - Seconds increment from 0 to 59, then reset to 0 and increment minutes.
  - Minutes increment from 0 to 59, then reset to 0 and increment hour.
  - The hour signal is a single bit that sets to 1 after reaching one hour.
- **Note**: The stopwatch will not count beyond one hour but can reset and restart from zero if reset occurs.

### Edge Cases and Special Handling:
- When the hour signal is set to 1, the stopwatch will hold its value at 1 hour, 0 minutes, and 0 seconds until the design is reset.
- If the stopwatch is paused mid-second, mid-minute, or mid-hour, it holds the current values of seconds, minutes, and hour, along with any partial progress within the ongoing count of input clock cycles. When start_stop is asserted high again, the stopwatch resumes counting from the exact point where it was paused.

### Assumptions and Limitations:
- Assume that the input frequency (CLK_FREQ) is set correctly within given constraints, for the design to generate a valid one-second pulse; invalid scenarios due to incorrect CLK_FREQ settings need not be handled.
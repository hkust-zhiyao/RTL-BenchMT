Design a **Finite State Machine (FSM)** sequence detector in System Verilog that detects the specific 8-bit sequence **`10110001`** from a continuous serial input. When the sequence is detected, the FSM should output a high signal for one clock cycle.

### Specification

#### Inputs
- `clk_in (1-bit)` - Input clock signal with 50% duty cycle to operate the design at the rising edge
- `rst_in (1-bit)` - Asynchronous active-high reset signal. When asserted high, the FSM resets to the initial state `S0`.
- `seq_in (1-bit)` - Serial input signal to provide a continuous stream of bits (`0` or `1`).

#### Output
- `seq_detected (1-bit)` - This signal is asserted HIGH for one clock cycle when the sequence `10110001` is detected otherwise remains at LOW

#### FSM Design Requirements

1. **State Definitions:**
   - Implement **eight states** (`S0` to `S7`) to represent each step in detecting the sequence.
   - **State Encoding**: Use a 3-bit state representation (`logic [2:0]`).

2. **Output Behavior:**
   - The output `seq_detected` should be **registered** and synchronized with `clk_in` to avoid glitches.
   - It should be asserted **only once** per detected sequence, for **one clock cycle** immediately after the last bit is received.

3. **Input Constraints:**
   - **`seq_in`** is always a valid binary input (`0` or `1`).
   - No special handling is required for invalid inputs.

4. **Sequence Overlaps:**
   - The FSM must handle overlapping sequences. For example, if `seq_in` contains `101100010110001`, the FSM should detect the sequence twice.

5. **Boundary Conditions:**
   - The FSM should correctly handle the sequence detection regardless of where it starts in the input stream.
   - There are no underflow or overflow conditions to consider.

6. **Timing Requirements:**
   - **State Transitions:** Occur on the rising edge of `clk_in`.
   - **Output Assertion:** `seq_detected` is asserted high on the rising edge of `clk_in` following the detection of the complete sequence.

---

**Implementation Details:**

- **Data Types:**
  - Use `bit` for the clock input `clk_in` for precise edge detection.
  - Use `logic` for other inputs and outputs.

- **State Representation:**
  - Define an enumerated type `state_t` for states `S0` to `S7` using `logic [2:0]`.

- **State Register:**
  - Implement a sequential always block triggered on `posedge clk_in` or `posedge rst_in` for state transitions.

- **Next State Logic:**
  - Use a combinational always block (`always_comb`) to determine `next_state` based on `cur_state` and `seq_in`.

- **Output Logic:**
  - Compute `seq_detected_w` in the combinational block.
  - Register `seq_detected` in a sequential always block to synchronize it with `clk_in`.

- **Reset Behavior:**
  - On assertion of `rst_in`, the FSM should immediately reset to `S0` and `seq_detected` should be cleared to `0`.

---
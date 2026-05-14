I need to implement a fixed constraint k=3 and a generator polynomial convolutional encoder in Verilog for a digital communication system. The encoder should have a constraint length k=3 and use two generator polynomials: \( g_1(x) = x^2 + x + 1 \) and \( g_2(x) = x^2 + 1 \). The encoder needs to take a serial input data stream and produce a 2-bit encoded output for each input bit.

The constraint length (K) is fixed at 3, which means the encoder uses the current input bit and the previous 2 bits (held in a 2-bit shift register) to generate the encoded outputs.

The generator polynomial g1 is "111", which corresponds to ( g_1(x) = x^2 + x + 1 ). This polynomial is used to generate the first encoded bit (encoded_bit1). The generator polynomial g2 is "101", which corresponds to ( g_2(x) = x^2 + 1 ). This polynomial is used to generate the second encoded bit (encoded_bit2).

The inputs to the module are:

1. clk: The clock signal used to synchronize the operations of the module.
2. rst: An asynchronous reset signal, active high. When asserted, it resets the shift register and the encoded output bits.
3. data_in: A single-bit input signal representing the incoming data stream to be encoded.

The outputs of the module are:

1. encoded_bit1: The first encoded output bit, generated using the generator polynomial g1.
2. encoded_bit2: The second encoded output bit, generated using the generator polynomial g2.
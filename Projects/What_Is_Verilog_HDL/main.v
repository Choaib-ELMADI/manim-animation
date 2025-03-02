module circuit (out, a, b);
    output reg  out;
    input  wire a;
    input  wire b;

    wire wire_1;
    wire wire_2;

    or  or_1  (wire_1, a, b);
    not not_1 (wire_2, b);
    and and_1 (out, wire_1, wire_2);

endmodule // circuit

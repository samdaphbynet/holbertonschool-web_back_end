const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", function () {
  describe("SUM operation", function () {
    it("should add two rounded numbers", function () {
      assert.strictEqual(calculateNumber("SUM", 1, 3), 4);
      assert.strictEqual(calculateNumber("SUM", 2, -2), 0);
      assert.strictEqual(calculateNumber("SUM", 1, -4), -3);

      assert.strictEqual(calculateNumber("SUM", 1.4, 5), 6);
      assert.strictEqual(calculateNumber("SUM", 1, 4.5), 6);
      assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
      assert.strictEqual(calculateNumber("SUM", 8, -8.2), 0);
      assert.strictEqual(calculateNumber("SUM", 7.8, -8), 0);
      assert.strictEqual(calculateNumber("SUM", 7.8, -8.2), 0);
      assert.strictEqual(calculateNumber("SUM", 3, -5.2), -2);
      assert.strictEqual(calculateNumber("SUM", 3.1, -5), -2);
      assert.strictEqual(calculateNumber("SUM", 3.1, -5.2), -2);

      assert.strictEqual(calculateNumber("SUM", 8.7), 9);
      assert.strictEqual(calculateNumber("SUM", 0.3), 0);
      assert.strictEqual(calculateNumber("SUM", -8.7), -9);
    });
  });

  describe("SUBTRACT operation", function () {
    it("should subtract b from a", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 5, 1), 4);
      assert.strictEqual(calculateNumber("SUBTRACT", 5, 5), 0);
      assert.strictEqual(calculateNumber("SUBTRACT", 1, 5), -4);

      assert.strictEqual(calculateNumber("SUBTRACT", 8.6, 4.1), 5);
      assert.strictEqual(calculateNumber("SUBTRACT", 8.6, 4), 5);
      assert.strictEqual(calculateNumber("SUBTRACT", 9, 4.1), 5);

      assert.strictEqual(calculateNumber("SUBTRACT", 10.2, 9.8), 0);
      assert.strictEqual(calculateNumber("SUBTRACT", 10.2, 10), 0);
      assert.strictEqual(calculateNumber("SUBTRACT", 10, 9.8), 0);

      assert.strictEqual(calculateNumber("SUBTRACT", 8.2, 9.2), -1);
      assert.strictEqual(calculateNumber("SUBTRACT", 8.2, 9), -1);
      assert.strictEqual(calculateNumber("SUBTRACT", 8, 9.2), -1);

      assert.strictEqual(calculateNumber("SUBTRACT", 8.7), 9);
      assert.strictEqual(calculateNumber("SUBTRACT", 0.3), 0);
      assert.strictEqual(calculateNumber("SUBTRACT", -8.7), -9);
    });
  });

  describe("DIVIDE operation", function () {
    it("should divide a by b", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1.6, 5.2), 0.4);
      assert.strictEqual(calculateNumber("DIVIDE", 1.6, 5), 0.4);
      assert.strictEqual(calculateNumber("DIVIDE", 2, 5.2), 0.4);
      assert.strictEqual(calculateNumber("DIVIDE", -1.6, 5.2), -0.4);
      assert.strictEqual(calculateNumber("DIVIDE", -1.6, 5), -0.4);
      assert.strictEqual(calculateNumber("DIVIDE", -2, 5.2), -0.4);
      assert.strictEqual(calculateNumber("DIVIDE", 1.6, -5.2), -0.4);
      assert.strictEqual(calculateNumber("DIVIDE", 1.6, -5), -0.4);
      assert.strictEqual(calculateNumber("DIVIDE", 2, -5.2), -0.4);
      assert.strictEqual(calculateNumber("DIVIDE", -1.6, -5.2), 0.4);
      assert.strictEqual(calculateNumber("DIVIDE", -1.6, -5), 0.4);
      assert.strictEqual(calculateNumber("DIVIDE", -2, -5.2), 0.4);

      assert.strictEqual(calculateNumber("DIVIDE", 0.3, 3.6), 0);
      assert.strictEqual(calculateNumber("DIVIDE", -0.3, 3.6), 0);
      assert.strictEqual(calculateNumber("DIVIDE", 0, 3.6), 0);
    });

    it('should return "Error" when dividing by 0', function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
      assert.strictEqual(calculateNumber(DIVIDE, 8.4, 0.4), "Error");
      assert.strictEqual(calculateNumber(DIVIDE, 8.4, -0.4), "Error");
      assert.strictEqual(calculateNumber(DIVIDE, 8.4, 0), "Error");
    });
  });
});

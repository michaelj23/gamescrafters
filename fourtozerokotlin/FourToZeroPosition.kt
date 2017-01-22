public class FourToZeroPosition() : Position() {
  public var num: Int = 0
  constructor(number: Int): this() {
    num = number
  }

  override fun equals(other: Any?): Boolean {
    if (other is FourToZeroPosition) {
      return other.num == num
    }
    return false
  }

  override fun hashCode(): Int {
    return num
  }
}

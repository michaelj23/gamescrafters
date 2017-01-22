public class FourToZero(): Game() {

  override fun initialPosition(): Position {
    return FourToZeroPosition(4)
  }

  override fun primitive(pos: Position): String {
    if (pos is FourToZeroPosition) {
      if (pos.num == 0) return LOSS
    }
    return UNDECIDED
  }

  override fun genMoves(pos: Position): Array<Move>? {
    if (pos is FourToZeroPosition) {
      if (pos.num >= 2) return arrayOf(FourToZeroMove(-1), FourToZeroMove(-2))
      return arrayOf(FourToZeroMove(-1))
    }
    return null
  }

  override fun doMove(pos: Position, move: Move): Position? {
    if (pos is FourToZeroPosition && move is FourToZeroMove) {
      return FourToZeroPosition(pos.num + move.moveNum)
    }
    return null
  }
}

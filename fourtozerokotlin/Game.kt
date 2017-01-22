public abstract class Game {
  companion object {
    val DRAW: String = "DRAW"
    val WIN: String = "WIN"
    val UNDECIDED: String = "UNDECIDED"
    val LOSS: String = "LOSS"
    val TIE: String = "TIE"
  }
  abstract fun initialPosition(): Position
  abstract fun primitive(pos: Position): String
  abstract fun genMoves(pos: Position): Array<Move>?
  abstract fun doMove(pos: Position, move: Move): Position?
}

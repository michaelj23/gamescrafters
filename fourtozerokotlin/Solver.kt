import java.util.HashMap
public class Solver(targGame: Game) {
  var game: Game = targGame
  var map = HashMap<Position, String>()
  fun solvePosition(curPos: Position): String {
    if (map[curPos] != null) {
      return map[curPos]!!
    }
    var result:String = game.primitive(curPos)
    if (result.equals(Game.UNDECIDED)) {
      var moves: Array<Move>? = game.genMoves(curPos)
      var newPositions: Array<Position?> = arrayOfNulls<Position>(moves!!.size)
      for (i in moves.indices) {
        newPositions[i] = game.doMove(curPos, moves[i])
      }
      result = Game.LOSS
      for (pos in newPositions) {
        if (solvePosition(pos!!).equals(Game.LOSS)) {
          result = Game.WIN
          break
        }
      }
    }
    map[curPos] = result
    return result
  }

  fun solve(): String {
    return solvePosition(game.initialPosition())
  }
}

fun main(args: Array<String>) {
  var solver: Solver = Solver(FourToZero())
  var solved: String = solver.solve()
  println("${solved}")
}

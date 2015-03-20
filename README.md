# functional-python

Functional programming inspires me and I try to find as many functional patterns that I can use even in imperative programming.
At first I wanted to see how I could implement the use of Monads in Python and I think it may evolve into something more, so I've left it
general.

## Typeclasses

* Functor:
    * `fmap`
* Applicative Functor:
    * `apply` _(`<*>` in Haskell)_
    * `pure`
* Monad:
    * `ret` _(`return` in Haskell)_
    * `bind` _(`>>=` in Haskell)_

## Data Types

* Identity
* Maybe
* Either

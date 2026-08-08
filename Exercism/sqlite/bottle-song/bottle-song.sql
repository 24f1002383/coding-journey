WITH RECURSIVE
  -- counts down from 10 to 0
  n(bottles) AS (
    SELECT 10
    UNION ALL
    SELECT bottles - 1 FROM n WHERE bottles > 0
  ),
  -- number-to-word lookup, including "No" for zero
  words(bottles, word) AS (
    SELECT 10, 'Ten' UNION ALL SELECT 9, 'Nine' UNION ALL
    SELECT 8, 'Eight' UNION ALL SELECT 7, 'Seven' UNION ALL
    SELECT 6, 'Six'  UNION ALL SELECT 5, 'Five'  UNION ALL
    SELECT 4, 'Four' UNION ALL SELECT 3, 'Three' UNION ALL
    SELECT 2, 'Two'  UNION ALL SELECT 1, 'One'   UNION ALL
    SELECT 0, 'No'
  ),
  verses(bottles, ord, line) AS (
    SELECT n.bottles, 1,
      w.word || ' green bottle' || CASE WHEN n.bottles = 1 THEN '' ELSE 's' END
      || ' hanging on the wall,'
    FROM n JOIN words w ON w.bottles = n.bottles WHERE n.bottles >= 1
    UNION ALL
    SELECT n.bottles, 2,
      w.word || ' green bottle' || CASE WHEN n.bottles = 1 THEN '' ELSE 's' END
      || ' hanging on the wall,'
    FROM n JOIN words w ON w.bottles = n.bottles WHERE n.bottles >= 1
    UNION ALL
    SELECT n.bottles, 3, 'And if one green bottle should accidentally fall,'
    FROM n WHERE n.bottles >= 1
    UNION ALL
    SELECT n.bottles, 4,
      'There''ll be ' || w.word || ' green bottle'
      || CASE WHEN n.bottles - 1 = 1 THEN '' ELSE 's' END
      || ' hanging on the wall.'
    FROM n JOIN words w ON w.bottles = n.bottles - 1 WHERE n.bottles >= 1
  )
SELECT line FROM verses ORDER BY bottles DESC, ord;